# -*- coding: utf-8 -*-
n = int(input("Введите количество элементов: "))
list = []
sum = 0
for n in range(n):
    a = int(input())
    list.append(a)
print(list)
for i in range(1, len(list), 2):
    sum+= list[i]
print(sum)



