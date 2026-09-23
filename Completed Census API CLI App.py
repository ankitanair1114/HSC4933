import requests

YEAR = 2020
DATASET = "dec/pl"
URL = f"https://api.census.gov/data/{YEAR}/{DATASET}"
API_KEY = "c58c124bd9ce8d7b057c2fb90406aa3aac45b9dc"

#Put in the inputs for both the geography FIPs codes/names and the variables
geography = input("Enter the State FIPS code(s) that you would like data for:")
variable = input("Enter the variable names that you would like data for:")

params = {
    "get": variable,
    "for": "state:" + geography,
    "key": API_KEY,
}

response = requests.get(URL, params=params)
response.raise_for_status()

if response.status_code != 200:
    print(f"Request failed ({response.status_code})")
    print(response.text)
    raise SystemExit(1)

data = response.json()

print (f"Got {len(data) - 1} rows back.")

for i in data:
    print(i)