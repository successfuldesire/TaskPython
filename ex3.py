list = [input() for _ in range(int(input()))]
obr = [float('0.' + (i.split('.')[1])) for i in list if '.' in i]
print(max(obr) - min(obr))