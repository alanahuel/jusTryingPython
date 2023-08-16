import requests
import re
from bs4 import BeautifulSoup 


url = 'https://www.escapefromtarkov.com/preorder-page'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

with open('tarkov_price.txt', 'w+') as file:
    for item in soup.find_all('span', {'itemprop':'price'}):
        price = item.text
        file.write(str(price) + "\n")