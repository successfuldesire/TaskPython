import math

xA = float(input("Введите координату xA: "))
yA = float(input("Введите координату yA: "))
xB = float(input("Введите координату xB: "))
yB = float(input("Введите координату yB: "))

result = math.sqrt((xA-xB)**2+(yA-yB)**2)
print(format(result, '.2f'))