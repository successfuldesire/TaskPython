src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq = set()
repeated = set()
for num in src:
    if num in repeated:
        continue
    if num in uniq:
        uniq.discard(num)
        repeated.add(num)
        continue
    uniq.add(num)
print([num for num in src if num in uniq])
