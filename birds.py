import requests
import sqlalchemy as db
import pandas as pd

# get_recent_observations
# 
# returns a list of dictionaries, each containing detailed information
# about individual bird observations from the eBird API. This includes 
# species names, observation dates and times, locations
#
# normal input: region_code and API key
# bad input: non-existent region code, API key. Extra parameters besides those in the function header or incorrect type of these

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
  # test for correct url construction, valid header and param dicts
  response = requests.get(url, headers=headers, params=params)
  
  if response.status_code == 200:
    return response.json()
  else:
    response.raise_for_status()

# *******************************************************************
if __name__ == "__main__":
  region_code = 'US-CA'  # Example region code for California
  api_key = 'epcc2hvf2vd7'  # authentication is my personal API key from eBird

  # testing: check for valid json file of observations (check eBird for sample return value from get request)
  # check that outupt from data engine is correct based on requirements and SQL query specifications.
  try:
    observations = get_recent_observations(region_code, api_key=api_key)
    
    # convert dictionary into a pandas dataframe:
    myFrame = pd.DataFrame.from_dict(observations)
    # create an engine and send all the data to a database. 
    # finally, print all the data results
    engine = db.create_engine('sqlite:///bird_database.db')
    myFrame.to_sql('bird_table', con=engine, if_exists='replace', index=False)
    with engine.connect() as connection:
      query_result = connection.execute(db.text("SELECT * FROM bird_table LIMIT 10;")).fetchall()
      print(pd.DataFrame(query_result))

    # print the observations (bird type, distance, location)
    # for observation in observations:
    #   print(f"{observation['comName']} observed on {observation['obsDt']} at {observation['locName']}")
  except Exception as e:
      print(f"Error: {e}")



