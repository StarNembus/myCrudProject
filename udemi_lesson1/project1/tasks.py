# Ваше задание: напишите игру крестики-нолики (Tic Tac Toe) на Python. Можете использовать любую среду разработки IDE.
#
# Требования следующие:
#
# В игру должны играть 2 игрока (оба за одним и тем же компьютером)
# На каждом ходе игрока, текущее состояние поля выводится на экран
# Вы должны получать на вход координаты клетки, куда следует поместить символ игрока, и затем помещать символ на поле

import random

# Напишите функцию, которая выводит на экран игровое поле. Поле можно хранить как список,
# где номера 1-9 соответствуют цифрам на цифровой клавиатуре. В итоге Вы получаете игровое поле 3 на 3.


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# test_board = [' '] * 10
# display_board(test_board)

# Напишите функцию, которая спрашивает пользователя, какой символ он хочет использовать, 'X' или 'O'.
# Можно например использовать цикл while,продолжая спрашивать до тех пор, пока пользователь
# не введёт корректный вариант ответа.


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Игрок 1: Кем Вы хотите играть, X или O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# player1_marker, player2_marker = player_input()
#
# print(player1_marker)


# Напишите функцию, которая принимает на вход объект игровое поле (список), символ ('X' или 'O'), желаемую позицию (число 1-9),
# и помещает этот символ на игровое поле

def place_marker(board, marker, position):
    board[position] = marker


# test_board = ['#', 'X', 'O', 'X', 'O', 'O', 'X', 'O', 'X']
# place_marker(test_board, '$', 8)
# display_board(test_board)

# Напишите функцию, которая берёт игровое поле, символ (X или O) и затем проверяет, выиграл ли этот символ.
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # горизонталь сверху
            (board[4] == mark and board[5] == mark and board[6] == mark) or # горизонталь в середине
            (board[1] == mark and board[2] == mark and board[3] == mark) or # горизонталь снизу
            (board[7] == mark and board[4] == mark and board[1] == mark) or # вертикаль слева
            (board[8] == mark and board[5] == mark and board[2] == mark) or # вертикаль в середине
            (board[9] == mark and board[6] == mark and board[3] == mark) or # вертикаль справа
            (board[7] == mark and board[5] == mark and board[3] == mark) or # диагональ
            (board[9] == mark and board[5] == mark and board[1] == mark)) # диагональ

# x = win_check(test_board, 'X')
# print(x)


# Напишите функцию, которая использует модуль random, чтобы случайным образом решить, какой из игроков ходит первым.
# Можете например использовать random.randint(). Верните строку с информацией о том, кто из игроков ходит первым.
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Игрок 2'
    else:
        return 'Игрок 1'

# Напишите функцию, которая возвращает значение boolean
# в зависимости от того, является ли указанное место на игровом поле пустым или нет.
def space_check(board, position):
    return board[position] == ' '

# Напишите функцию, которая проверяет, является ли игровое поле полностью заполненным,
# и возвращает значение boolean - True если полностью заполнено, иначе False.
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Напишите функцию, которая запрашивает у игрока следующую позицию (как число 1-9),
# и затем использует функцию с шага 6 чтобы проверить, является ли эта позиция пустой.
# Если да, то возвращает эту позицию для дальнейшего использования.
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Выберите следующую клетку: (1-9) '))

    return position

# Напишите функцию, которая спрашивает игрока, хочет ли он сыграть снова, и возвращает True если игрок говорит "да".
def replay():
    return input('Вы хотите сыграть снова? Yes или No: ').lower().startswith('y')


import time

# Запуск игры
print('Добро пожаловать в игру Крестики-Нолики!')
time.sleep(0.2)

while True:
    # Настройка игры
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('Первым ходит ' + turn + '.')

    play_game = input('Вы готовы играть? Введите Yes или No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок 1':
            # Ход Игрока 1

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Поздравляю! Вы выиграли!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 2'

        else:
            # Ход Игрока 2

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Игрок 2 выиграл!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 1'

    if not replay():
        break