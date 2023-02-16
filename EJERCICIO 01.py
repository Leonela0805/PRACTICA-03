# 1. Crea un programa en Python que simule una lista de compras. 
# El programa debe permitir al usuario agregar productos al final de la lista, 
# eliminar productos del inicio de la lista y mostrar todos los productos en la lista en orden de compra.

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None
    
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
        
    def agregar_ultimo(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente=Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1
        

    def eliminar_inicio(self):
        if self.vacia():
            return
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1
    
    
try:
    if __name__ == "__main__":
        opcion = 0
        listaCompra = ListaDoble()
        while opcion != 4:
            print('Lista compras: \n 1. Agregar \n 2. Eliminar \n 3. Mostrar\n 4. Salir')
            opcion = int(input('Ingrese opcion '))
            if opcion == 1:
                compra = str(input('Ingrese compra (producto): '))
                listaCompra.agregar_ultimo(compra)
            elif opcion == 2:
                dato = listaCompra[0]
                listaCompra.eliminar_inicio(dato)
            elif opcion == 3:
                listaCompra.recorrido()
            elif opcion == 4:
                print('FIN')
            else:
                print('Ingrese un dato correcto')

except Exception as e:
    print(e)