import requests

def get_recent_observations(region_code, days_back=14, hotspot=False, include_provisional=False, max_results=None, spp_locale='en', api_key='YOUR_EBIRD_API_KEY'):
    url = f'https://api.ebird.org/v2/data/obs/{region_code}/recent'
    
    params = {
        'back': days_back,
        'hotspot': str(hotspot).lower(),
        'includeProvisional': str(include_provisional).lower(),
        'sppLocale': spp_locale
    }
    
    if max_results is not None:
        params['maxResults'] = max_results
    
    headers = {
        'x-ebirdapitoken': api_key
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    region_code = 'US-CA'  # Example region code for California
    api_key = 'epcc2hvf2vd7'  # authentication is my personal API key

    try:
        observations = get_recent_observations(region_code, api_key=api_key)
        for observation in observations:
            print(f"{observation['comName']} observed on {observation['obsDt']} at {observation['locName']}")
    except Exception as e:
        print(f"Error: {e}")
