list_1 = [int(input()) for _ in range(int(input()))]
list_2 = []
for i in range(len(list_1) // 2 + len(list_1) % 2):
    list_2.append(list_1[i] * list_1[len(list_1) -1 -i])
print(list_2)