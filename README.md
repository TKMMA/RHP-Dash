GFA Dashboard: The Reef Habitat Plan (v3.3.26)

The GFA Dashboard is an exceptionally niche interactive spatial analysis tool developed by TK for DAR. It visualizes community feedback on reef restoration methods across Hawaiʻi’s Moku (districts), providing decision-makers with raw data and population-adjusted statistical outliers.

🚀 Launch Live Dashboard
📊 Core Features
1. View Modes
Raw Counts: Displays the absolute volume of survey responses. This is the primary "heatmap" of community engagement.

Outlier Mode: Normalizes response data against 2025 Total Population (sum_TOTPOP_CY). This identifies areas where community interest is statistically higher or lower than the state average per capita.

2. Statistical Metrics
Diverging Floating Bars: In Outlier Mode, charts center on the "Somewhat Effective" category.

Positive Float: High "Most Effective" sentiment relative to population.

Negative Float: High "Hardly Effective" sentiment relative to population.

Representation Gap: Calculates the percentage point difference between a Moku's share of the state population and its share of the total survey responses.

Density Ratio: Displays the "1 Response per X People" metric to gauge sample depth.

3. Interactive GIS Components
Static Map Labels: Live response counts displayed over each Moku polygon.

Dynamic Choropleth: Map coloring in Outlier Mode updates based on which restoration filters (e.g., Art. Reefs, Fish Stocking) are selected.

Selection Reset: Click any open ocean area on the map to return to the Statewide Overview.

🛠 Technical Architecture
This dashboard is a serverless "Live" application. It does not rely on static CSV/JSON files for its data; instead, it queries ArcGIS REST API endpoints directly upon page load.

Mapping Engine: Leaflet.js

Chart Engine: Chart.js with the datalabels plugin.

Primary Data Source: RHP SURVEY - View layer

Geospatial Source: Moku with population layer

📂 Repository Structure
index.html: Contains the entire application logic (HTML5, CSS3, and JavaScript).

survey_data.json: (Legacy/Backup) Contains a hardcoded snapshot of initial survey data. Note: The live dashboard currently bypasses this for the REST API.
