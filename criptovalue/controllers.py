 #control de la logica
from criptovalue.models import CriptoValueModel
from criptovalue.views import CriptoValueView

class CriptoValueController():
    def __init__(self):
        self.modelo = CriptoValueModel()
        self.vista = CriptoValueView()

    def ejecuta(self):
        seguir = 's'
        while seguir == 's':
            self.modelo.de, self.modelo.a = self.vista.pedir()
            self.modelo.obtener()
            self.vista.muestra(self.modelo.de, self.modelo.a, self.modelo.valor)

            seguir = input("Quieres más (S/N): ").lower() 
