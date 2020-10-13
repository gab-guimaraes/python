import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python-3.x'

response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

#print(response.text)

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')

    print(titulo.text)
