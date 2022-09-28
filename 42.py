import random


sleep(2)
print('\nРешение')

list_rand = [(random.randint(1, 10)) for n in range(10)]
print(f'Случайный список сформирован {list_rand}')

list_unic = []
for i in range(len(list_rand)):
        if list_rand[i] not in list_rand[i+1:] and list_rand[i] not in list_rand[:i]:
            list_unic.append(list_rand[i])
print(list_unic)
print('___________________________________________________________________________________')
