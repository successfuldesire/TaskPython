from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
rez = zip_longest(tutors, klasses)
rez = tuple(rez)
for i in range(len(rez)):
  if rez[i][0] == None:
    continue
  print(rez[i])

