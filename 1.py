from interface import Interface
from api import Api_acceso


def main():
    board_flag = input("Usar el tablero predeterminado?, si, no: ")
    if board_flag == "si":
        board = ["53xx7xxxx",
                 "6xx195xxx",
                 "x98xxxx6x",
                 "8xxx6xxx3",
                 "4xx8x3xx1",
                 "7xxx2xxx6",
                 "x6xxxx28x",
                 "xxx419xx5",
                 "xxxx8xx79"]
    elif board_flag == "no":
        difficulty = input("Dificultad: 1, 2, 3: ")
        api_accesso = Api_acceso(difficulty)
        board = api_accesso.get_new_board()

    interface_sudoku = Interface(board)
    show_board(interface_sudoku.get_board())
    over = False

    while not over:
        number = input("number: ")
        Y = input("Y: ")
        X = input("X: ")
        board, over = interface_sudoku.play(number, X, Y)
        show_board(board)
    print("Felicidades, ha completado el juego")


def show_board(board):
    if len(board) == 9:
        for line in board:
            print(line)
    else:
        print(board)


main()