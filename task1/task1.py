"""напишите функцию slice_less,
на вход принимает:
1. первый аргумент “my_list” - список из целых чисел
2. второй аргумент “lesser” - целое число
выводит:
отсортированный от большего к меньшему список my_list, где все значения больше чем lesser
"""


def slice_less(my_list, lesser):
    print(sorted([x for x in my_list if x > lesser], reverse=True))


if __name__ == '__main__':
    list_ = [1, 2, 3, 4, 5, 6]
    slice_less(list_, 3)
