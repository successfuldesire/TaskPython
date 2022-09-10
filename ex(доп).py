import random
n = int(input())
list = []
for i in range(n):
    list.append(random.randint(-n, n))
f = open("gg", "r")
a = f.read().splitlines()
sum = 1
for i in a:
    sum *= list[int(i)]
print(sum)