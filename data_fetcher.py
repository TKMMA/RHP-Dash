import requests
import json

# The specific Service IDs from your ArcGIS layers
SURVEY_LAYER_URL = "https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/RHP_SURVEY_-_View_layer_-_no_emails/FeatureServer/0/query"
MOKU_LAYER_URL = "https://services.arcgis.com/HQ0xoN0EzDPBOEci/ArcGIS/rest/services/Moku%20with%20population%20and%20point%20count/FeatureServer/0/query"

def fetch_arcgis_data(url):
    params = {
        'where': '1=1',
        'outFields': '*',
        'f': 'json',
        'resultOffset': 0
    }
    response = requests.get(url, params=params)
    return response.json().get('features', [])

def process_dashboard_data():
    # Fetching raw data from your ArcGIS layers
    survey_data = fetch_arcgis_data(SURVEY_LAYER_URL)
    
    # Example logic: Grouping "Artificial Reefs" by Moku
    dashboard_json = {}
    for feature in survey_data:
        attr = feature['attributes']
        moku = attr.get('MOKUSELECTED_where_do_you_restr', 'Unknown')
        rating = attr.get('Artificialreefs')
        
        if moku not in dashboard_json:
            dashboard_json[moku] = {"Most": 0, "Somewhat": 0, "Hardly": 0}
        
        if rating == "Most effective": dashboard_json[moku]["Most"] += 1
        elif rating == "Somewhat effective": dashboard_json[moku]["Somewhat"] += 1
        elif rating == "Hardly effective": dashboard_json[moku]["Hardly"] += 1

    # Save for the GitHub Dashboard to use
    with open('survey_highlights.json', 'w') as f:
        json.dump(dashboard_json, f, indent=4)
    print("Data synced for RHP-Dash!")

if __name__ == "__main__":
    process_dashboard_data()
