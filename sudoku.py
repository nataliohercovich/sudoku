import math

class Sudoku():
    def __init__(self, tablero):
        self.tablero = tablero
        self.longitud = len(self.tablero)
        self.zona = int(math.sqrt(self.longitud))        
        self.no_borrar = []
        self.valores_fijos()
 
    """guarda coordenadas valores fijos"""

    def valores_fijos(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if (self.tablero[i][j] != 0):
                    self.no_borrar.append((i , j))

    """no modificar valores fijos"""

    def no_cambiar(self, x, y):

        if (x, y) in self.no_borrar:
            return False
        else:
            return True        
            
    """no repetir valores en filas"""

    def no_repetir_fila(self, x, n):
        
        if (n in self.tablero[x]):
            return False
        else:
            return True
            

    """no repetir valores en columna"""

    def no_repetir_columna(self, y, n):
        
        for i in self.tablero:
            if (i[y] == n):
                return False
            else:
                return  True
    
       
    """no repetir valor en zona"""

    def no_repetir_zona (self, x, y, n):

        
        if (x < self.zona):
            x = 0
        elif (x >= self.zona and x <= (self.zona * 2)):
            x = self.zona
        else:
            x = self.zona * 2

        for i in range(self.zona):
            for j in range(self.zona):
                if self.tablero[x + i][x + j] == n:
                    return False
        return True

    """poner numero"""

    def poner_numero(self, x, y, n):

        if self.no_cambiar(x, y) and self.no_repetir_fila(x, n) and self.no_repetir_columna(y, n) and self.no_repetir_zona(x, y, n):

            self.tablero[x][y] = n
            
            return True
        else:
            return False

    def gano(self):

        for i in self.tablero:
            
            if (0 in i):

                return False
        return True

    

 

   


        
