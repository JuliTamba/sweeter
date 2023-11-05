import requests 

api_key = 'c650d953-f613-479a-ab86-d984e7bdddb0'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/${word}?key=${api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definitions) 