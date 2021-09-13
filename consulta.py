import requests

url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"   #dejo los huecos para poder pedir lo que quedamos
apikey = "9A55ADFB-B569-458B-BFA9-77AE8D360889"

cabecera = {"X-Coinapi-Key": apikey}
respuesta = requests.get(url, headers=cabecera)   #petición

if respuesta.status_code == 200:
    print(respuesta.text)