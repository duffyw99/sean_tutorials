import requests

"""
Intro to the python response library and using Application Programming Interfaces (APIs)

We're going to ask OpenWeatherMap for the current weather via their api.
OpenWeatherMap needs to know:
a) who we are, via our api key
b) the location where we want to know the weather. There are a few options for this, so we'll use zip code since it's easy
"""

## api key is free, sent via email when you submit a request
## Details at: https://openweathermap.org/appid
api_key = 'replace_with_your_api_key'

## the api takes a zip as a parmeter and sends back weather info
zip_code = '32252'

## prepare a string that contains the api's url along with your query parameters (after the "?")
## I'm using an 'f-string' to plug in my varibles: https://realpython.com/python-f-strings/
## The old way was to use ".format(var1, var2)" at the end; this is much easier to read
api_url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&zip={zip_code}'

## send that url string to the internet as a GET request (becuase we're using it to 'get' something back)
## learn more about the requests library: https://docs.python-requests.org/en/master/
r = requests.get(api_url)

## if it worked, you now have a 'request object' called 'r' with the info you got back from your request
## so 'r' now has some propeties: a status_code (did your request work?), headers, encoding, and text.
#print(r.status_code)
#print(r.headers)
#print(r.encoding)
#print(r.text)

## most of that is 'meta-data'; data about your data. The weather data is in the r.text object
## right now r.text is just a string, but it's in json format. Let's create a copy of that string, but converted into json
import json
json_response_text = json.loads(r.text)

## lets make that prettier to read (just for us humans; this isn't a necessary step)
import pprint
pprint.pprint(json_response_text)

## you should have a big meaty 'dictionary' of info in json_response_text.
## dictionaries (dicts) in python are very useful objects
## they contain 'key:value' pairs. You ask the dict for a key, you get the value back
print(json_response_text['name'])

## sometimes the value is another 'nested' group of key:value pairs, like the latitude and longitude of our zipcode
print(json_response_text['coord'])

## so we can drill down into THAT by asking for the key within a key
print(json_response_text['coord']['lat'])

## so far, everything has been in {curly brackets}, making them dicts
## but there's another type of collection here with [square brackets], which is a list
print('weather is a list: ' + str(json_response_text['weather']))

## this example stinks because it's a list with only 1 thing in it, and it's a list of dicts
## I think it's designed this way because you can request a forecast from this api, so
## typically it will be a list of weather now, weather in an hour, weather in 2hrs, etc.
## Lists don't have 'keys', so you have to ask for values based on their position in the list
## First, second, third, etc.. That position is called the Index, and it starts with zero
example_list = ['first_list_item','second_list_item','third_list_item']
## print the value at index 'zero'
print(example_list[0])
## print the value at index 'two'
print(example_list[2])

## let's look at our list in 'weather' again
print(json_response_text['weather'])
## the 'weather' list only has one thing in it, so let's look at index 0
print(json_response_text['weather'][0])

## and there's a dict there (notice the square brackets went away), so we can go back to using key names
print(json_response_text['weather'][0]['description'])


## this process of getting stuff out of dicts and lists is called 'list comprehension'.
## for a weather-based wallpaper script, we'll need the weather conditions.
## maybe we'd want to take temp into account to... but let's keep it simple for now

## Let's look at the weather API website docs to see if there's something useful there
## https://openweathermap.org/current#list -> https://openweathermap.org/weather-conditions

## looking at that, I think the numeric id field is going to be easier to use than the wordy description
## it's simpler to program: ids that start with 3 are all types of rain, ids that start with 2 are lightning, etc
## than to enter in all those lengthy descriptions.

## this is information we're going to use in our code, so let's assign the id a variable
weather_code = json_response_text['weather'][0]['id']
## and confirm it worked:
print(weather_code)
