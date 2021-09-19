from criptvalue.models import CriptoValueModel
from criptvalue import APIKEY, URL

model = CriptoValueModel()

seguir= = 's'

while seguir == 's':
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")

    modelo.obtener(de,a)
    print(modelo.valor)

    seguir = input("Quieres mas monedas? (S/N) ").lower()
