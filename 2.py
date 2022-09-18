def find_division(n):
    dividers = []
    for i in range(2, n + 1):
        while n % i == 0:
            dividers.append(i)
            n //= i
    return list(set(dividers))
print(find_division(34156))
