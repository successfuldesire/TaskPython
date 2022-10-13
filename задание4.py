my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(**kwargs)


biggest_dict(one=22, two=31, three=11, four=91)
print(my_dict)