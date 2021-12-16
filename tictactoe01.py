# указываем месторасположение наших ходов по цифрам на цифровой клавиатуре:
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

# обновляем нашу игровую доску после каждого хода созданием функции:
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# основная функция с игрой будет выглядеть следующим образом:
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Твой ход, " + turn + ". Куда двигаться?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Эта клетка заполнена.\nКуда двигаться?")
            continue

        # проверка победителя после 5 ходов в игре:
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # заполена первая строка
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # заполена вторая строка
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # заполена третья строка
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # заполнен первый столбец
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # заполнен второй столбец
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # заполнен третий столбец
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # заполнена одна диагональ
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # заполнена вторая диагональ
                printBoard(theBoard)
                print("\nИгра окончена.\n")
                print(" **** " + turn + " победил. ****")
                break

                # Если победитель так и не выявлен после девятого хода, тогда объявляем ничью:
        if count == 9:
            print("\nИгра окончена.\n")
            print("Ничья в игре!!")

        # осуществляем с помощью инструкции смену игроков после каждого хода:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # вопрос о перезапуске игры:
    restart = input("Хотите повторить игру?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()

# когда интерпретатор Python читает исходный файл,
# он исполняет весь найденный в нем код. Перед тем, как начать выполнять команды,
# он определяет несколько специальных переменных. Например,
# если интерпретатор запускает некоторый модуль (исходный файл) как основную программу,
# он присваивает специальной переменной __name__ значение "__main__".
# Если этот файл импортируется из другого модуля, переменной __name__ будет присвоено имя этого модуля.
# простыми словами: Переменная __name__ равна __main__ только в точке входа в программу - в скрипте переданном интерпретатору при запуске:
if __name__ == "__main__":
    game()
