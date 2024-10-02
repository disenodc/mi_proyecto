# gbif_utils.py
import requests

def fetch_gbif_occurrence_data(taxon_key, limit=300):
    url = f"https://api.gbif.org/v1/occurrence/search"
    params = {
        "taxonKey": taxon_key,
        "limit": limit,
        "offset": 0
    }
    all_results = []
    
    while True:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            all_results.extend(data['results'])
            params['offset'] += limit

            # Check if there are more results to fetch
            if params['offset'] >= data['count']:
                break
        else:
            raise Exception("Failed to fetch data from GBIF")
    
    return all_results
