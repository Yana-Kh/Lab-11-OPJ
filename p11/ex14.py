
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Введите строку: ")


def test_input(s):
    return s.isdigit()


def str_to_int(s):
    return int(s)


def print_int(i):
    print(i)


if __name__ == '__main__':
    a = get_input()
    if test_input(a):
        print_int(str_to_int(a))
    else:
        print("Строка не является целым числом")
