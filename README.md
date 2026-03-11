GFA Dashboard: The Reef Habitat Plan (v3.3.26)

The GFA (Geographic Focus Area) Dashboard is an interactive, and exceptionaly niche, spatial analysis tool developed by TK for DAR. It serves as a decision-support platform for Goal 3 of the Makai Restoration Action Plans within the broader Hawaiʻi Coral Reef Strategy (HCRS) 2030.

🌊 Project Context
From July 2024 to April 2025, DAR’s Fisheries Liaison engaged extensively with fishers across all islands through in-person events and social media. This dashboard visualizes the results of a Survey123 that received over 1,000 responses from Hawaiʻi’s nearshore fishing community.

The goal is to translate community input on how and where fish habitat could be improved into a written action plan directly informed by those who know the resource best.

🚀 Launch Live Dashboard

📊 Core Features
1. Dual-View Analysis
Raw Counts: Visualizes the absolute volume of community feedback. This is essential for identifying areas with high stakeholder engagement.

Outlier Mode: Adjusts data based on the 2025 Total Population (sum_TOTPOP_CY). This prevents high-population urban centers from overshadowing the voices of smaller, rural fishing communities, allowing managers to see where interest "stands out" per capita.

2. Statistical Metrics
Diverging Floating Bars: Charts center on the "Somewhat Effective" category to show sentiment shifts. Bars floating into positive territory indicate a higher-than-average belief in a method's effectiveness relative to the local population.

Representation Gap: A real-time calculation showing if a Moku is over- or under-represented in the survey data compared to its share of the state population.

Density Ratio: Displays the "1 Response per X People" metric to gauge the statistical "weight" of the local feedback.

3. Interactive GIS Components
Static Map Labels: Live response counts sit permanently over each Moku for instant readability.

Restoration Filters: Managers can toggle between six specific methods (e.g., Invasive Limu Removal, Artificial Reefs) to see how priorities shift geographically.

Hover Discovery: Hover over any polygon to confirm the specific Moku district name.

🛠 Technical Architecture
This is a serverless, live-querying application. It does not use static data files; it fetches live updates directly from DAR's ArcGIS infrastructure.

Mapping Engine: Leaflet.js

Chart Engine: Chart.js

Data Sources: * RHP SURVEY - View layer

Moku with Population Layer

📂 Related Resources
For more background on the geospatial analysis and project milestones, visit the RHP Links & Resources document.

Developed by TK for the State of Hawaiʻi Division of Aquatic Resources.
