import requests

url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"   #dejo los huecos para poder pedir lo que quedamos
apikey = "9A55ADFB-B569-458B-BFA9-77AE8D360889"

cabecera = {"X-CoinAPI-Key": apikey}
respuesta = requests.get(url, headers=cabecera)   #petición

print(respuesta.status_code)
#midiccionario = respuesta.json()    también lo podemos hacer así
#print(midiccionario['rate'])

print(respuesta.json()['rate'])


