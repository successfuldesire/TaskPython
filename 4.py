import random

k = int(input())
x1 = random.randint(1, 100)
x2 = random.randint(1, 100)
x3 = random.randint(1, 100)
vir = (f'при k = {k} => {x1}x^{k} + {x2}x + {x3}')
print(vir)
with open('chisla.txt', 'w') as n:
    n.write(vir)