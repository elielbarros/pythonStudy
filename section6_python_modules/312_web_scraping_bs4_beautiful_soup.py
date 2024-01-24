"""
# English
+ Web Scraping with Python using requests and bs4 BeautifulSoup
- Web Scraping is the act of "scraping the web" searching for information in a
automated, with a specific programming language, for later use.
- The requests module can load data from the Internet into your
code. bs4.BeautifulSoup is responsible for interpreting HTML data
in Python object format to make the developer's life easier.
- Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
+ Installation
- pip install requests types-requests bs4

# Portuguese
+ Web Scraping com Python usando requests e bs4 BeautifulSoup
- Web Scraping é o ato de "raspar a web" buscando informações de forma
automatizada, com determinada linguagem de programação, para uso posterior.
- O módulo requests consegue carregar dados da Internet para dentro do seu
código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
em formato de objetos Python para facilitar a vida do desenvolvedor.
- Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
+ Instalação
- pip install requests types-requests bs4
"""
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3000/'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# How print TITLE website
print(parsed_html.title)  # output: <title>SITE</title>

# How print TITLE text website
if parsed_html.title is not None:
    print(parsed_html.title.text)  # output: SITE


