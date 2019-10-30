import unittest

from sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    
    def test_valores_fijos_ok(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        self.assertNotEqual (sudoku.no_borrar, [(0, 3), (0, 1), (0, 4), (1, 0), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 7), (3, 0), (3, 4), (3, 8), (4, 0), (4, 3), (4, 5), (4, 8), (5, 0), (5, 4), (5, 8), (6, 1), (6, 6), (6, 7), (7, 3), (7, 4), (7, 5), (7, 8), (8, 4), (8, 7), (8, 8)])


    def test_valores_fijos_mal(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        self.assertEqual (sudoku.no_borrar, [(0, 0), (0, 1), (0, 4), (1, 0), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 7), (3, 0), (3, 4), (3, 8), (4, 0), (4, 3), (4, 5), (4, 8), (5, 0), (5, 4), (5, 8), (6, 1), (6, 6), (6, 7), (7, 3), (7, 4), (7, 5), (7, 8), (8, 4), (8, 7), (8, 8)])

    def test_no_cambiar_ok(self):

        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_cambiar(0,3)
        self.assertTrue(resultado)

    def test_no_cambiar_mal(self):

        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_cambiar(0,0)
        self.assertFalse(resultado)

    def test_no_repetir_fila_ok(self):

        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_repetir_fila(3,3)
        self.assertFalse(resultado)

    def test_no_repetir_fila_mal(self):
    
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_repetir_fila(1,4)
        self.assertTrue(resultado)

    def test_no_repetir_columna_ok(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_repetir_columna(1,2)
        self.assertTrue(resultado)

    def test_no_repetir_columna_mal(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_repetir_columna(1,3)
        self.assertFalse(resultado)


    def test_no_repetir_zona_mal(self):
            
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_repetir_zona(0,8,6)
        self.assertFalse(resultado)

    def test_no_repetir_zona_ok(self):
                       
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.no_repetir_zona(1,1,2)
        self.assertTrue(resultado)


    def test_no_repetir_zona4_ok(self):
            
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])

        resultado = sudoku.no_repetir_zona(1,1,1)
        self.assertTrue(resultado)

    def test_no_repetir_zona4_mal(self):
            
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])

        resultado = sudoku.no_repetir_zona(1,1,4)
        self.assertFalse(resultado)


    def test_poner_numero_mal(self):
    
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.poner_numero(0,0,0)
        self.assertFalse(resultado)

    def test_poner_numero_ok(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

        resultado = sudoku.poner_numero(1,1,2)
        self.assertTrue(resultado)
        
    def test_gano_ok(self):
        
        sudoku = Sudoku ([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]])

        resultado = sudoku.gano()
        self.assertTrue(resultado)

    



if __name__ == '__main__':

    unittest.main()