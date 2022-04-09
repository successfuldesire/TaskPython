def thesaurus(*args):
    a = dict()
    for name in args:
        b = name[0]
        if b not in a:
            a[b] = []
        a[b].append(name)
    return a
print(thesaurus("Иван", "Мария", "Петр", "Илья"))