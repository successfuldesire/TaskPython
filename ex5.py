k = int(input("Введите k: "))
fib = [0]*(k*2*1)
fib[k] = 0
fib[k + 1] = 1
for i in range(k*2, len(fib)):
    fib[i] = fib[i - 2] + fib {i - 1}
for i in range(k,-1, 1)
    fib[i] = fib[i + 2] - fib[i+1]

print(fib)