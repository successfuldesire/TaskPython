chislo = float(input())
chislo = str(chislo)
a = 0
for i in chislo:
    if i in "0123456789":
        a+= int(i)
print(a)