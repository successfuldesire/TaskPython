def func(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
if (func(0, 0, 0) and func(0, 0, 1) and func(0, 1, 0) and
func(0, 1, 1) and func(1, 0, 0) and func(1, 0, 1) and
func(1, 1, 0) and func(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")
