# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

min = int(input("Введите минимум диапазона: "))
max = int(input("Введите максимум диапазона: "))
list_input = list()
list_result = list()
list_input = [int(i) for i in input().split(",")]
for i in range(len(list_input)):
    if list_input[i] > min and list_input[i] < max:
        list_result.append(i)   
print(list_result)