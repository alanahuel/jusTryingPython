import requests

url = 'https://www.racksmafia.com/'
response = requests.get(url)

with open('output.txt', 'w+') as file:
    file.write(response.text)
    