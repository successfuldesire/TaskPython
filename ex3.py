list = []
n = int(input())
a = 0
def func(x):
    return (1 + (1/x))**x
for i in range(1, n):
    list.append(func(n))
for i in list:
    a = a + i
print(a)
