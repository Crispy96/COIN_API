class CriptoValueView():
    def pedir(self):
        de = input("Moneda de origen: ")
        a = input("Moneda de destino: ")

        return de, a

    def muestra(self, origen, destino, valor):
        print(f"1 {origen} vale {valor} {destino}") 