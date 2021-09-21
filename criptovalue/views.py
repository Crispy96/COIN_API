from tkinter import *   #usado para crear interfaces gráficas
from tkinter import ttk
from criptovalue._init_ import MONEDAS

class CriptoValueView():
    def pedir(self):
        de = input("Moneda de origen: ")
        a = input("Moneda de destino: ")

        return de, a

    def muestra(self, origen, destino, valor):
        print(f"1 {origen} vale {valor} {destino}") 

def funcion_del_boton():
    print("Click")

#frame(parent,option) es como un contenedor

class Exchanger(ttk.Frame):
    def __init__(self, parent, funcion_click_del_controlador):
        super().__init__(parent, height=300, width=430)

        self.grid_propagate(0)   #sirve para que el contenedor se adapte al tamaño y no al contenido

        self.desde_valor = StringVar()
        self.desde = ttk.Combobox(self, values=MONEDAS, textvariable = self.desde_valor)
        self.desde.grid(column=0, row=0)

        self.hasta_valor = StringVar()    #monedas para escoger
        self.hasta = ttk.Combobox(self, values=MONEDAS, textvariable = self.hasta_valor)
        self.hasta.grid(column=1, row=0)

        self.valor = ttk.Label(self, anchor=CENTER, text="0.0")    #texto
        self.valor.grid(column=0, row=1, columnspan=2)

        self.calcular = ttk.Button(self, text="Calcular", command=funcion_click_del_controlador)   #boton, command llama a un paramatro
        self.calcular.grid(column=1, row=2)

    def moneda_desde(self):
        return self.desde_valor.get()[:3]    #le pido que me coja el texto hasta el valor que queramos

    def moneda_hasta(self):
        return self.hasta_valor.get()[:3]

    def set_valor(self, texto):
        self.valor.config(text=texto)
