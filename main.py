import requests

headers = {'X-Api-Key': 'aabd2b6970694484a9a90e970cd037ba'}
urlType = 'https://randommer.io/api/Card/Types'
urlCard = 'https://randommer.io/api/Card'
r = requests.get(urlType, headers=headers)
data = r.json()


params = {'type' : data[1]}
r2 = requests.get(urlCard, params=params, headers=headers)
data2 = r2.json()
print(data2)

