import pandas as pd

# From Google Sheets to Pandas - Mandatory for Dash
df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vROnXww3tyLDg0lLkHFQz4X1Xd-DhLJF4J0-R8VYhVCXgUkZhPAwMa3c52nzzWqzbgCG4YZiJQVXQyQ/pub?output=csv')

print(df.head())

# From Pandas to JSON - Mandatory for Highcharts 
json = df.to_json(orient='split')

print(json)