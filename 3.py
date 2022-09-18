import random

def find_unique(k):
    counter = 0
    unique = []
    while counter <= k:
        unique.append(random.randint(0, 100))
        counter += 1
    return list(set(unique))

print(find_unique(55))