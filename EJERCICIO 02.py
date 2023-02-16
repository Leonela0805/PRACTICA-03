# 2. Crea un programa en Python que mantenga un historial de tareas pendientes. 
# El programa debe permitir al usuario agregar una tarea al inicio de la lista, 
# eliminar una tarea del final de la lista y mostrar todas las tareas en la lista en orden inverso al que se agregaron. 
# Además, el programa debe contar la cantidad total de tareas en la lista y mostrar ese número al usuario.

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

    def inverso(self):
        aux = self.primero
        lista = []
        while aux != None:
            aux = aux.siguiente
            dato1 = aux.dato
        lista.append(dato1)
        print(lista.reverse())

            
    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.primero  = self.primero
            self.primero = aux
        self.size += 1
    
    def eliminar_final(self):
        if self.vacia():
            print('Lisa vacía')
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            aux = self.ultimo
            aux.anterior = self.ultimo
            self.ultimo.siguiente = None
            self.size -= 1

    def cantidadTareas(self):
        cantidad = self.size
        print('La cantidad de total de tareas pendientes es: ', cantidad)

try:
    if __name__ == "__main__":
        opcion = 0
        historialTareas = ListaDoble()
        while opcion != 6:
            print('\t\t\tHISTORIAL DE TAREAS\t\t\t \n 1. Agregar tarea \n 2. Eliminar última tarea \n 3. Mostrar recorrido inicial \n 4. Mostrar orden inverso de tareas \n 5. Cantidad de tareas pendientes \n 6. Salir')
            opcion = int(input('Ingrese opcion: '))
            if opcion == 1:
                tarea = str(input('\nIngrese tarea: '))
                historialTareas.agregar_inicio(tarea)
            elif opcion == 2:
                historialTareas.eliminar_final()
            elif opcion == 3:
                historialTareas.recorrido()
            elif opcion == 4:
                historialTareas.inverso()
            elif opcion == 5:
                historialTareas.cantidadTareas()
            elif opcion == 6:
                print('FIN')
            else:
                print('Ingrese un dato correcto')

except Exception as e:
    print(e)