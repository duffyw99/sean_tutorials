import json
import requests

## api key is free, sent via email when you submit a request
## Details at: https://openweathermap.org/appid
api_key='replace_with_your_api_key' 
zip_code = '32252'

## prepare api url string
api_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&zip={zip_code}'

## submit request and get response object back
r = requests.get(api_url)

## format response data into json and pull current weather value
json_response_text = json.loads(r.text)
weather_code = json_response_text['weather'][0]['id']

## evaluate weather code with the documentation from the api website
## https://openweathermap.org/weather-conditions
## determine if the code between the lower and upper limits of each 'bucket' from the documentation
if 200 <= weather_code < 300:
    weather = 'thunder'
if 300<=weather_code<400:
    weather = 'drizz'
if 500<=weather_code<600:
    weather = 'rain'
if 600<=weather_code<700:
    weather = 'snow'
if 700<=weather_code<800:
    weather = 'atmosphere'
## some codes we want to drill into, so we'll look at the specifc code
if weather_code==781:
    weather = 'tornado'
if weather_code in (800,801):
    weather = 'clear'
if weather_code in (802,803,804):
    weather = 'cloudy'

## sanity check
print(weather)
