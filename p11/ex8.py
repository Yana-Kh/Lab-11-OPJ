# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    a = int(input("Введите число: "))
    if a > 0:
        positive(a)
    elif a == 0:
        print("а = 0")
    else:
        negative(a)


def positive(a):
    print("Положительное")


def negative(a):
    print("Отрицательное")


if __name__ == '__main__':
    test()
