# GFA Dashboard: The Reef Habitat Plan (v4.2)

The **GFA (Geographic Focus Area) Dashboard** is an interactive spatial analysis tool developed by TK for DAR. It serves as a decision-support platform for **Goal 3** of the [Makai Restoration Action Plans](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing) within the broader [Hawaiʻi Coral Reef Strategy (HCRS) 2030](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing).

##  [Launch Dashboard](https://tkmma.github.io/RHP-Dash/)

##  Project Context
From July 2024 to April 2025, DAR's Fisheries Liaison engaged extensively with fishers across all islands through in-person events and social media. This dashboard visualizes the results of a **Survey123** that received roughly **1,100 responses** from Hawaiʻi's nearshore fishing community, rating six restoration methods and (optionally) naming where they'd like to see restoration happen.

The goal is to translate community input on **how and where fish habitat could be improved** into a written action plan directly informed by those who know the resource best.

---

##  The Three Map Views
The map answers three different questions about the same feedback. Toggle between them at the top of the panel; click any Moku to drill in, click the ocean to return statewide.

| View | Question it answers | How it's colored |
|------|--------------------|------------------|
| **Responses** | *Where did people engage the most?* | Sequential blue by raw response count — the absolute volume of feedback. |
| **Participation** | *Where does the community speak up out of proportion to its size?* | A **location quotient**: a Moku's share of responses ÷ its share of state population, centered on **1.0**. Blue = louder than its population share, red = quieter. |
| **Sentiment** | *Where are the selected methods rated most / least favorably?* | Smoothed average favorability vs. the statewide mean. Blue = above average, red = below. |

> The **Responses** and **Participation** maps count every response regardless of method, so they are unaffected by the method filters. The **Sentiment** map and the opinion chart respond to the filters — a response is a response, but favorability is method-specific.

---

##  Statistical Modeling & Calculations
The central modeling problem is **normalization**: a handful of dense urban Moku hold most of the state's population *and* most of the raw responses, which can drown out smaller rural fishing communities — while at the same time a single response in a near-empty district can masquerade as a dramatic "outlier." Every metric below is designed so that small, rural districts are neither buried nor turned into false signal.

### Three response totals (they differ on purpose)
Because the location question was **optional** when the survey first launched, the denominators aren't all the same, and each metric uses the correct one:

| Count | ~ | Used for |
|------|----|----------|
| Total responses | **1,094** | Overall engagement |
| Answered the effectiveness questions ("opinion-bearing") | **1,017** | Statewide favorability & sentiment |
| Also named a restoration Moku | **990** | Everything per-district (participation, per-Moku sentiment) |

Responses that rated the methods but named no district still count toward the *statewide* opinion; they simply can't be placed on the map.

### 1. Participation — Location Quotient
A classic location quotient compares a district's *share of voice* to its *share of population*:

```
LQ(moku) = (moku responses / total mapped responses) ÷ (moku population / state population)
```

It is **centered on 1.0 by construction** and is independent of the method filters, so "average participation" always reads as 1.0. `LQ > 1` means a district is over-represented in the survey relative to its population; `LQ < 1`, under-represented. The map's diverging blue↔red ramp is keyed to `log₂(LQ)`, so 2× over and 2× under are visually symmetric.

### 2. Sentiment — favorability, then shrinkage
Each ordinal rating is mapped to a number, and a Moku's favorability is the mean across its respondents and the **selected** methods:

```
score:  Most effective → 1.0   Somewhat effective → 0.5   Hardly effective → 0
favorability(moku) = mean( score )  over (respondents × selected methods)
```

Using the full ordinal scale (not just the "Most effective" count) makes this a proper sentiment measure that is independent of how *many* people responded. The statewide mean **μ** is the same average taken over all **1,017** opinion-bearing responses — that's the baseline the map diverges around.

Raw per-Moku averages are noisy where few people responded, so favorability is smoothed with **Empirical-Bayes shrinkage** toward μ:

```
shrunk(moku) = ( Σ score  +  K·μ ) / ( N_ratings  +  K )      where  K = 8 × (selected methods)
```

`K` is a prior worth ~**8 respondents**. A Moku with ~8 responses lands halfway between its own average and the state average; a Moku with hundreds barely moves; a Moku with one respondent sits almost exactly at μ. This prevents a lone voice from painting an entire district an extreme color, without hiding it. The map colors each Moku by `shrunk − μ`.

### 3. Method ranking — net favorability
The opinion chart's x-axis can be sorted by each method's **net favorability** for the current scope:

```
net(method) = %(Most effective) − %(Hardly effective)
```

The chart loads sorted statewide. The order is **sticky** when you select a Moku (so positions stay put for comparison); the **Sort** button re-ranks to the selected district on demand, and highlights itself when the current order no longer matches that district's ranking.

### 4. Small-sample handling
Two complementary safeguards:

* **Suppression (Participation).** A per-capita rate is meaningless when the denominator is tiny, so districts under **500 residents** or **5 responses** are drawn in grey ("insufficient data") rather than assigned a misleading extreme. This is why uninhabited districts (e.g. Kahoʻolawe, Niʻihau) no longer dominate the map, and why the panel hides the per-capita ratio there while still showing the honest percentage-point gap.
* **Shrinkage (Sentiment).** Rather than a hard cutoff, small districts are pulled toward the state mean (above), so they read as "about average" instead of vanishing. The panel additionally flags any district with fewer than **5** responses.

> **Tuning:** the thresholds (`MIN_POP = 500`, `MIN_RESP = 5`), the shrinkage strength (`SHRINK_K = 8`), and the ordinal `SCORE` map live at the top of the `<script>` block in `index.html` and are documented inline for easy adjustment.

---

##  The Opinion Chart
For the selected scope, the six methods are broken out by rating with several ways to read them:

* **Diverging (default)** — a Likert view with zero at the midpoint of "Somewhat effective," so methods leaning right are net-favored and methods leaning left are net-doubted. Good for seeing the *balance* of opinion.
* **100% Stacked** — each bar runs 0–100% with "Most" on top and "Hardly" on the bottom, so shares are directly comparable across methods.
* **Single Column / Stepped** — overlap the three ratings into one column, or step them side-by-side.
* **Sort by ranking** — order the methods by net favorability (see above).

Bars are expressed as a **% of respondents**, which keeps them comparable across districts of any size. (Percent is the right scale for cross-district comparison; absolute counts are reserved for static figures in the written plan, where "685 of 1,017 fishers" carries more weight.)

##  Panel Metrics
* **Participation.** The location quotient and the percentage-point gap between a Moku's response share and its population share (the ratio is suppressed for districts below the reporting thresholds).
* **Density Ratio.** The "1 Response per X People" metric, to gauge the statistical weight of local feedback.
* **Sentiment.** The Moku's smoothed favorability vs. the statewide average.
* **Small-sample flag.** Districts below the response threshold are labeled so managers know when to treat a reading with caution.

##  Interactive GIS Components
* **Permanent Map Labels:** Live response counts sit permanently over each Moku for instant readability.
* **Restoration Filters:** Toggle six methods (e.g. *Invasive Limu Removal*, *Artificial Reefs*) to see how **Sentiment and the opinion chart** shift.
* **Hover Discovery:** Hover over any polygon to confirm the specific Moku district name; click to drill in.

---

##  Technical Architecture
This is a serverless, live-querying application. It fetches live updates directly from DAR's ArcGIS infrastructure on every load — there are no static data files.

* **Mapping Engine:** [Leaflet.js](https://leafletjs.com/) (CartoDB Positron basemap)
* **Chart Engine:** [Chart.js](https://www.chartjs.org/) with the datalabels plugin
* **Data Sources:**
    * [RHP SURVEY - View layer](https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/RHP_SURVEY_-_View_layer_-_no_emails/FeatureServer/0?f=pjson) (~1,094 responses; ~1,017 rated the methods; ~990 map to a specific restoration Moku via `MOKUSELECTED_where_do_you_restr`)
    * [Moku with Population Layer](https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/Moku%20with%20population%20and%20point%20count/FeatureServer/0?f=pjson) (46 districts, 2025 population estimates in `sum_TOTPOP_CY`, ~1.48M statewide)

All aggregation (per-Moku counts, favorability, location quotients, shrinkage, ranking) is computed **client-side** from the live features, so the analysis always reflects the current survey data.

---

##  Related Resources
For more background on the geospatial analysis and project milestones, visit the [RHP Links & Resources](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing) document.

**Developed by TK for the State of Hawaiʻi Division of Aquatic Resources.**
