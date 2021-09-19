from criptovalue.models import CriptoValueModel

modelo = CriptoValueModel()  #lo instancio

seguir = 's'
while seguir == 's':
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")

    modelo.obtener(de, a)
    print(modelo.valor)

#esto e  s lo mismo que en consulta1 del 12-20

    seguir = input("Quieres más (S/N): ").lower()
