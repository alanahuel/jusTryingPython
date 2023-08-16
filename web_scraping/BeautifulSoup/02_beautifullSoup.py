import requests
import re
from bs4 import BeautifulSoup 

url = 'https://www.racksmafia.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


# Capturar HTML

with open('beautiful.txt', 'w+') as file:
    file.write(soup.prettify())


# Capturar etiquetas

with open('links.txt','w+') as file:
    for link in soup.find_all('a'):
        href = link.get('href')
        file.write(href + '\n')



# Capturar links con el atributo en específico

with open('onlyHTTP.txt', 'w+') as f:
    for link in soup.find_all('a', attrs={'href':re.compile("^http")}):
        href = link.get('href')
        f.write(href + '\n')

# Navegar por el árbol de análisis

body = soup.body
body_contents = body.contents 

with open('body_content.txt', 'w+', encoding='utf-8') as f:
    for content in body_contents:
        f.write(str(content))


