import random
def get_jokes(res):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    for _ in range(res):
        joke.append(f"{nouns[random.randint(0, 4)]} {adverbs[random.randint(0, 4)]} {adjectives[random.randint(0, 4)]}")
    return joke
n = 3
print(get_jokes(n))

