import requests

class CountryInfo:
    def __init__(self, url):
        self.url = url
        self.data = None
    
    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Failed to retrieve data")
    
    def display_countries_and_currencies(self):
        if self.data is None:
            print("Data not fetched yet")
            return
        
        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")
    
    def display_countries_with_currency(self, currency_name):
        if self.data is None:
            print("Data not fetched yet")
            return
        
        countries = []
        for country in self.data:
            currencies = country.get('currencies', {})
            for currency_info in currencies.values():
                if currency_info.get('name', '').lower() == currency_name.lower():
                    countries.append(country.get('name', {}).get('common', 'N/A'))
                    break
        
        if countries:
            print(f"Countries with {currency_name}: {', '.join(countries)}")
        else:
            print(f"No countries found with currency: {currency_name}")
    
    def display_countries_with_dollar(self):
        self.display_countries_with_currency('dollar')
    
    def display_countries_with_euro(self):
        self.display_countries_with_currency('euro')

# Usage
url = "https://restcountries.com/v3.1/all"
country_info = CountryInfo(url)
country_info.fetch_data()
country_info.display_countries_and_currencies()
country_info.display_countries_with_dollar()
country_info.display_countries_with_euro()
