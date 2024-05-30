import requests
import pandas as pd

# Function to get breweries by state
def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}&per_page=100"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {state}")
        return []

# List of states
states = ['Alaska', 'Maine', 'New York']

# Dictionary to store breweries data
breweries_data = {state: get_breweries_by_state(state) for state in states}

# 1. List the names of all breweries present in the states of Alaska, Maine and New York.
def list_breweries_names():
    for state in states:
        print(f"\nBreweries in {state}:")
        for brewery in breweries_data[state]:
            print(brewery['name'])

# 2. What is the count of breweries in each of the states mentioned above?
def count_breweries():
    for state in states:
        print(f"{state} has {len(breweries_data[state])} breweries.")

# 3. Count the number of types of breweries present in individual cities of the state mentioned above
def count_brewery_types_by_city():
    for state in states:
        print(f"\nBrewery types in cities of {state}:")
        df = pd.DataFrame(breweries_data[state])
        city_type_counts = df.groupby(['city', 'brewery_type']).size().unstack(fill_value=0)
        print(city_type_counts)

# 4. Count and list how many breweries have websites in the states of Alaska, Maine and New York.
def count_breweries_with_websites():
    for state in states:
        count = sum(1 for brewery in breweries_data[state] if brewery['website_url'])
        print(f"{state} has {count} breweries with websites.")
        print(f"Breweries with websites in {state}:")
        for brewery in breweries_data[state]:
            if brewery['website_url']:
                print(f"{brewery['name']}: {brewery['website_url']}")

# Run the functions
list_breweries_names()
count_breweries()
count_brewery_types_by_city()
count_breweries_with_websites()
