import requests
import pandas as pd

# Make an API request and get the response in JSON format
response = requests.get("API_URL_HERE")
data = response.json()

# Convert the JSON data to a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel spreadsheet
df.to_excel("data.xlsx")
