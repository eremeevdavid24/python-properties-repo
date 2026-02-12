import requests

api_key = '79d0658a01b34e2384480665c9545166'
url = (f'https://newsapi.org/v2/everything?q=tesla&from='
       '2026-02-05&sortBy='
       f'publishedAt&apiKey={api_key}')


# cerere
request = requests.get(url)

# otinem un dict (dictionary) cu date
content = request.json()

# accesarea titlui si descrierii articolului
for article in content['articles']:
    print(article['title'])
    print([article['description']])


