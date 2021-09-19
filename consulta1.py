import requests

apikey = "9A55ADFB-B569-458B-BFA9-77AE8D360889"
url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"

cabecera = {"X-CoinAPI-Key": apikey}

seguir = 's'
while seguir == "s":
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")
    respuesta = requests.get(url.format(de,a), headers=cabecera)

    if respuesta.status_code == 200:
        print(respuesta.json()["rate"])
    else:
        print(respuesta.status_code)
        print(respuesta.json())

    seguir = input("Quieres más (S/N)").lower()
   