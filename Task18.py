# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
#    1 2 3 4 5
#   6 -> 5

N = int(input("Какое количество элементов будет содержать ваш массив? : ")) # запрос на размерность массива А
A = list() # создали пустой список для элементов массива А
for i in range (N):
    X = int(input("Введите число массива: "))
    A.append(X) # В цикле добавляем в список А вводимые пользователем элементы Х

k = int(input("Введите заданное число: ")) 
Modul = abs(k - A[0]) # вводим модуль разницы заданного числа и первого элемента списка А
Ablizk = A[0] # присвоили самому близкому числу значение первого элемента введённого списка А
for i in range(1, len(A)): # для всех элементов списка А проверяем условие
    if Modul > abs(A[i] - k): # если модуль текущей разницы меньше предыдущего значения модуля, то
        Modul = abs(A[i] - k) # мы текущую разницу называем модулем и
        Ablizk = A[i] # присваиваем текущее число списка А переменной, содержащей близкое значение.
print ("Самым близким по величине элементом к вашему числу", k, "будет число", Ablizk)