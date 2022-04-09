def new_translate(num):
    nums = {"one": "один", "two": "два", "tree": "три", "four": "четыре", "five": "пять",
            "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    return nums.get(num)


print(new_translate(input("")))