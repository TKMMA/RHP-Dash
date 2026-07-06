# GFA Dashboard: The Reef Habitat Plan (v4.0)

The **GFA (Geographic Focus Area) Dashboard** is an interactive spatial analysis tool developed by TK for DAR. It serves as a decision-support platform for **Goal 3** of the [Makai Restoration Action Plans](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing) within the broader [Hawaiʻi Coral Reef Strategy (HCRS) 2030](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing).

##  [Launch Dashboard](https://tkmma.github.io/RHP-Dash/)

## 🌊 Project Context
From July 2024 to April 2025, DAR's Fisheries Liaison engaged extensively with fishers across all islands through in-person events and social media. This dashboard visualizes the results of a **Survey123** that received over **1,000 responses** from Hawaiʻi's nearshore fishing community.

The goal is to translate community input on **how and where fish habitat could be improved** into a written action plan directly informed by those who know the resource best.

---

## 📊 The Three Map Views
The map answers three different questions about the same feedback. Toggle between them at the top of the panel; click any Moku to drill in, click the ocean to return statewide.

| View | Question it answers | How it's colored |
|------|--------------------|------------------|
| **Responses** | *Where did people engage the most?* | Sequential blue by raw response count — the absolute volume of feedback. |
| **Participation** | *Where does the community speak up out of proportion to its size?* | A **location quotient**: a Moku's share of responses ÷ its share of state population, centered on **1.0**. Blue = louder than its population share, red = quieter. |
| **Sentiment** | *Where are the selected methods rated most / least favorably?* | Average favorability vs. the statewide mean. Blue = above average, red = below. |

## 📐 Methodology
The analysis is intentionally conservative so that small, rural districts are neither drowned out nor turned into false outliers.

* **Location Quotient (Participation).** `(responses / total responses) ÷ (population / state population)`. This is filter-independent and centered on 1.0 by construction, so "average" always reads as 1.0 regardless of how many methods are selected. Values above 1 mean a district is over-represented in the survey relative to its population; below 1, under-represented.
* **Favorability score (Sentiment).** Each response is scored **Most = 1.0, Somewhat = 0.5, Hardly = 0**, then averaged across the selected methods. This uses the full ordinal scale (not just the "Most effective" count) and is independent of how many people responded.
* **Empirical-Bayes shrinkage.** A district's favorability is pulled toward the statewide mean in proportion to how few people responded there. A district with ~8 responses lands halfway between its own average and the state average; a district with hundreds barely moves. This prevents a lone respondent from painting an entire Moku an extreme color.
* **Small-sample suppression.** Per-capita rates are meaningless when the denominator is tiny, so districts under **500 residents** or **5 responses** are shown in grey ("insufficient data") rather than assigned a misleading value. This is why uninhabited districts (e.g. Kahoʻolawe, Niʻihau) no longer dominate the outlier map.

## 📈 Panel Metrics
* **Diverging Opinion Chart.** For the selected scope, each method is shown as a diverging (Likert) bar expressed as a **% of respondents**. Zero sits at the midpoint of "Somewhat effective," so methods leaning right are net-favored and methods leaning left are net-doubted — directly comparable across districts of any size.
* **Participation.** The location quotient and the percentage-point gap between a Moku's response share and its population share.
* **Density Ratio.** The "1 Response per X People" metric, to gauge the statistical weight of local feedback.
* **Small-sample flag.** Districts below the response threshold are labeled so managers know when to treat a reading with caution.

## 🗺 Interactive GIS Components
* **Permanent Map Labels:** Live response counts sit permanently over each Moku for instant readability.
* **Restoration Filters:** Toggle six methods (e.g. *Invasive Limu Removal*, *Artificial Reefs*) to see how **Sentiment and the opinion chart** shift. (Responses and Participation count all feedback and are unaffected by the filters — a response is a response regardless of method.)
* **Hover Discovery:** Hover over any polygon to confirm the specific Moku district name.

---

## 🛠 Technical Architecture
This is a serverless, live-querying application. It fetches live updates directly from DAR's ArcGIS infrastructure on every load — there are no static data files.

* **Mapping Engine:** [Leaflet.js](https://leafletjs.com/)
* **Chart Engine:** [Chart.js](https://www.chartjs.org/)
* **Data Sources:**
    * [RHP SURVEY - View layer](https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/RHP_SURVEY_-_View_layer_-_no_emails/FeatureServer/0?f=pjson) (~1,090 responses; ~990 map to a specific restoration Moku)
    * [Moku with Population Layer](https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/Moku%20with%20population%20and%20point%20count/FeatureServer/0?f=pjson) (46 districts, 2025 population estimates)

> **Tuning:** the thresholds above (`MIN_POP`, `MIN_RESP`, `SHRINK_K`) and the effectiveness scores live at the top of the `<script>` block in `index.html` and are documented inline for easy adjustment.

---

## 📂 Related Resources
For more background on the geospatial analysis and project milestones, visit the [RHP Links & Resources](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing) document.

**Developed by TK for the State of Hawaiʻi Division of Aquatic Resources.**
