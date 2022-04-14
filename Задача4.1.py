N = 15
def odd_nums(N):
    for odd_to_15 in range (1, N+1):
        if odd_to_15 % 2 != 0:
            print(odd_to_15)
            yield odd_to_15
odd_to_15 = odd_nums(N)


next(odd_to_15)
next(odd_to_15)
next(odd_to_15)