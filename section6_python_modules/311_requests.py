"""
# English
- requests -
Popular library for making HTTP requests. It simplifies the process of sending HTTP requests and handling the responses. The library is known for being easy to use and offering a user-friendly interface for working with web APIs and performing HTTP communication.

How to install?
pip install requests

How to get?
response = requests.get('https://www.example.com')
print(response.text)

How to post?
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://www.exemplo.com/post', data=data)
print(response.text)

Tutorial -> https://youtu.be/Qd8JT0bnJGs

# Portuguese
- requests -
Biblioteca popular para fazer requisições HTTP. Ele simplifica o processo de envio de solicitações HTTP e o manuseio das respostas. A biblioteca é conhecida por ser fácil de usar e oferecer uma interface amigável para trabalhar com APIs web e realizar comunicação HTTP.

Como instalar?
pip install requests

Como fazer get?
response = requests.get('https://www.exemplo.com')
print(response.text)

Como fazer post?
data = {'chave1': 'valor1', 'chave2': 'valor2'}
response = requests.post('https://www.exemplo.com/post', data=data)
print(response.text)

Tutorial -> https://youtu.be/Qd8JT0bnJGs
"""
import requests

# If the website starts with http:// -> so it is on port 80
# If the website starts with https:// -> so it is on port 443
url = 'http://localhost:3000/'

response = requests.get(url)

print(response, response.status_code)  # output: <Response [200]> | 200
# print(response.content)  # output: Html Using format bytes b'<!DOCTYPE
print(response.text)  # output: HTML Text

# It is possible to convert response into JSON with:
# response.json()
