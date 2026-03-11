# GFA Dashboard: The Reef Habitat Plan (v3.3.26)

The **GFA (Geographic Focus Area) Dashboard** is an exceptionally niche interactive spatial analysis tool developed by TK for DAR. It serves as a decision-support platform for **Goal 3** of the [Makai Restoration Action Plans](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing) within the broader [Hawaiʻi Coral Reef Strategy (HCRS) 2030](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing).

## 🌊 Project Context
From July 2024 to April 2025, DAR’s Fisheries Liaison engaged extensively with fishers across all islands through in-person events and social media. This dashboard visualizes the results of a **Survey123** that received over **1,000 responses** from Hawaiʻi’s nearshore fishing community. 

The goal is to translate community input on **how and where fish habitat could be improved** into a written action plan directly informed by those who know the resource best.

## 🚀 [Launch Live Dashboard](https://tkmma.github.io/RHP-Dash/)

---

## 📊 Core Features

### 1. Dual-View Analysis
* **Raw Counts:** Visualizes the absolute volume of community feedback. This is essential for identifying areas with high stakeholder engagement.
* **Outlier Mode:** Adjusts data based on the **2025 Total Population** (`sum_TOTPOP_CY`). This prevents high-population urban centers from overshadowing the voices of smaller, rural fishing communities, allowing managers to see where interest "stands out" per capita.

### 2. Statistical Metrics
* **Diverging Floating Bars:** In Outlier Mode, charts center on the "Somewhat Effective" category to show sentiment shifts. Bars floating into positive territory indicate a higher-than-average belief in a method's effectiveness relative to the local population.
* **Representation Gap:** A real-time calculation showing if a Moku is over- or under-represented in the survey data compared to its share of the state population.
* **Density Ratio:** Displays the "1 Response per X People" metric to gauge the statistical "weight" of the local feedback.

### 3. Interactive GIS Components
* **Permanent Map Labels:** Live response counts sit permanently over each Moku for instant readability.
* **Restoration Filters:** Managers can toggle between six specific methods (e.g., *Invasive Limu Removal*, *Artificial Reefs*) to see how priorities shift geographically on the map.
* **Hover Discovery:** Hover over any polygon to confirm the specific Moku district name.

---

## 🛠 Technical Architecture
This is a serverless, live-querying application. It does not use static data files; it fetches live updates directly from DAR's ArcGIS infrastructure.

* **Mapping Engine:** [Leaflet.js](https://leafletjs.com/)
* **Chart Engine:** [Chart.js](https://www.chartjs.org/)
* **Data Sources:** * [RHP SURVEY - View layer](https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/RHP_SURVEY_-_View_layer_-_no_emails/FeatureServer/0?f=pjson)
    * [Moku with Population Layer](https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/Moku%20with%20population%20and%20point%20count/FeatureServer/0?f=pjson)

---

## 📂 Related Resources
For more background on the geospatial analysis and project milestones, visit the [RHP Links & Resources](https://docs.google.com/document/d/1yZgAC0Bs_O5a_DOmwVkMjCMVveab1P2VcyMG6-hPV_Q/edit?usp=sharing) document.

**Developed by TK for the State of Hawaiʻi Division of Aquatic Resources.**
