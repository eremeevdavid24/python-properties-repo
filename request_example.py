import requests

api_key = '79d0658a01b34e2384480665c9545166'
url = (f'https://newsapi.org/v2/everything?q=tesla&from='
       '2026-01-05&sortBy='
       f'publishedAt&apiKey={api_key}')

request = requests.get(url)
content = request.json
print(content)

