import requests

response = requests.get("http://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-512gb/space-grev/p3834614")

print(response.content)