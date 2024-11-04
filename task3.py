num = int(input('Введите количество элементов: '))
i = 0
list_num = []

while i < num:
    list_num.append(int(input('Введите ваше число: ')))
    i += 1

print('Ваш список: ')
print(list_num)

for i in range(len(list_num) - 1):
    for j in range(len(list_num) - 1 - i):
        if list_num[j] > list_num[j + 1]:
            list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]

print('Отсортированный список: ')
print(list_num)