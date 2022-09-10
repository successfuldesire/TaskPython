n = int(input())
list = [1]
for i in range(2, n+1):
    list.append(list[i-2]*(i))
print(list)