import requests
import time
import json

# Global variabel til at gemme data
data_store = []

# Extract-function
def extract():
    url = "https://api.energidataservice.dk/dataset/Elspotprices?offset=0&sort=HourUTC%20desc&timezone=dk&limit=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['records']
    else:
        print("Fejl ved hentning af data:", response.status_code)
        return []

# Transform-function
def transform(data):
    transformed_data = []
    for record in data:
        transformed_record = {
            "HourUTC": record["HourUTC"],
            "PriceArea": record["PriceArea"],
            "SpotPriceDKK": record["SpotPriceDKK"],
        }
        transformed_data.append(transformed_record)
    return transformed_data

# Load-function
def load(data):
    global data_store
    data_store.extend(data)  
    
    with open("elspotprices.json", "w") as f:
        json.dump(data_store, f, indent=4)
    
    print("Data gemt i elspotprices.json")

# Main-function
def main():
    while True:
        print("Henter data...")
        raw_data = extract()
        if raw_data:
            print("Transformerer data...")
            transformed_data = transform(raw_data)
            print("Gemmer data...")
            load(transformed_data)
        else:
            print("Ingen data hentet.")
        
        print("Venter på næste hentning...")
        time.sleep(3600)  # Pause i 1 time

# Start ETL-processen
if __name__ == "__main__":
    main()
