from api import api

from sudoku import Sudoku

class Interfaz():

    def pedir_longitud(self):

        self.longitud = 0
        self.tablero =  ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        
        self.juego = Sudoku(self.tablero)

        

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
        
        while not self.juego.gano():
            print(self.juego.getTable())

            self.pedir_valores()
            if self.ingresar_numero(self.n , self.x , self.y):
                print(self.juego.poner_numero(int(self.n) , int(self.x)-1 , int(self.y)-1))
    
            else:
                print("Ingrese un numero del 1 al 9")

        print("\n FIN")

if __name__ == "__main__":
    juego = Interfaz()
    
    juego.jugar()    


