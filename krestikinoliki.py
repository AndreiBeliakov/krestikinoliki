a = [int(x) for x in range(1, 10)]  # задаем список от 1 до 9
k = 1  # задаем счетчик ходов
print("... ход 1 ...")
while not (
        a[0] == a[1] == a[2] or a[3] == a[4] == a[5] or a[6] == a[7] == a[8] or a[0] == a[3] == a[6] or a[1] == a[4] ==
        a[7] or a[2] == a[5] == a[8] or a[0] == a[4] == a[8] or a[2] == a[4] == a[6]):#условие победы
    print(".............")
    print(":", a[0], ":", a[1], ":", a[2], ":")
    print(".............")
    print(":", a[3], ":", a[4], ":", a[5], ":")
    print(".............")
    print(":", a[6], ":", a[7], ":", a[8], ":")
    print(".............")#отображение игрового поля
    if k % 2 == 1 and k < 10:#программа проверяет, чей сейчас ход (если нечетный ход-нолики, если четный-крестики)
        b = input("введите позицию для нолика:") #ввод позиции на игровом поле
        if b != str(1) and b != str(2) and b != str(3) and b != str(4) and b != str(5) and b != str(6) and b != str(
                7) and b != str(8) and b != str(9):#программа проверяет, что введены числа,соотвествующие позициям на игровом поле
            print("ошибка ввода")#если символ не соответствует позиции, выводится ошибка
            print("....ход", k, "...")
        else:
            z = int(b)#если позиция введена правильна, определяем символ как целое число
            if a[z - 1] == 'О':#программа проверяет, что на поле,которое задает игрок, отсутсвует нолик
                print('здесь уже стоит нолик')
            elif a[z - 1] == 'X':#программа проверяет, что на поле,которое задает игрок, отсутвует крестик
                print('здесь уже стоит крестик')
            else:#если игрок не допустил ошибок, программа ставит нолик в поле
                a[z - 1] = 'О'
                k = k + 1#счетчик ходов
            print("... ход", k, "...")
    elif k % 2 == 0 and k < 10:#аналогично алгоритму для нолика
        b = input("введите позицию для крестика:")
        if b != str(1) and b != str(2) and b != str(3) and b != str(4) and b != str(5) and b != str(6) and b != str(
                7) and b != str(8) and b != str(9):
            print("ошибка ввода")
            print("... ход", k, "...")
        else:
            z = int(b)
            if a[z - 1] == 'О':
                print('здесь уже стоит нолик')
            elif a[z - 1] == 'X':
                print('здесь уже стоит крестик')
            else:
                a[z - 1] = 'X'
                k = k + 1
            print("....ход", k, "...")
    else:#если на 10 ход не выявлен победитель, программа объявляет ничью
        print("ничья")
        exit(0)
print(".............")
print(":", a[0], ":", a[1], ":", a[2], ":")
print(".............")
print(":", a[3], ":", a[4], ":", a[5], ":")
print(".............")
print(":", a[6], ":", a[7], ":", a[8], ":")
print(".............")
if k % 2 == 0:#программа определяет, какая команда победила
    print("победили нолики")
else:
    print("победили крестики")
