"""
# English
Before execute this module execute the command:
python -m http.server -d section6_python_modules/310_http_server/ 3000

# Portuguese
Antes de executar este module execute o comando:
python -m http.server -d section6_python_modules/310_http_server/ 3000
"""
import re  # Regular Expression

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3000/'

response = requests.get(url)
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    print(top_jobs_heading.text)  # output: TOP 3 jobs
    # Article Text
    # Getting parent
    article = top_jobs_heading.parent

    if article is not None:
        # print(article.text)
        for p in article.select('p'):
            # print(p.text)
            # using regular expression to remove more than one space to only one space
            print(re.sub(r'\s{1,}', ' ', p.text).strip())

