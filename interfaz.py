from api import api

from sudoku import Sudoku

class Interfaz():

    def pedir_longitud(self):

        self.longitud = 0
        self.tablero = api(self.longitud)
        self.juego = Sudoku(self.tablero)

        while self.longitud != "9" and self.longitud != "4":
            self.longitud = input("Ingrese el tamaño del tablero (4 o 9)")

            if self.longitud != "9" and self.longitud != "4":
                print ("Ingrese 9 o 4 \n\n")
            
        self.longitud = int(self.longitud)

    def ingresar_numero(self, x, y, n):
        try:
            if int(x) > self.longitud:
                return False
            elif int(y) > self.longitud:
                return False
            elif n != 0:
                if int(n) > 0 and int(n) < self.longitud+1:
                    return  True
            else:
                return True
        except Exception:
            return False

    def pedir_valores(self):
        self.n = input("Ingrese un numero: ")
        self.x = input("Ingrese numero de fila: ")
        self.y = input("Ingrse numero de columna: ")
        print("")

    def jugar(self):

        self.pedir_longitud()
        print("")
        print(self.juego.getTable())

        while not self.juego.getTable():
            self.pedir_valores()
            if self.ingresar_numero(self.n , self.x , self.y):
                print(self.juego.poner_numero(self.n , int(self.x)-1 , int(self.y)-1))
    
            else:
                print("Ingrese un numero del 1 al 9")

        print("\n FIN")

if __name__ == "__main__":
    juego = Interfaz()
    juego.jugar()


        
