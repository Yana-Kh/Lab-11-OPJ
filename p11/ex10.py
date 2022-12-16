# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))

    def circle():
        skruga = math.pi * r ** 2
        return skruga

    choice = input("S боковой поверхности (1), S цилиндра (2): ")
    if choice == '1':
        print(2 * math.pi * r * h)
    elif choice == '2':
        print(circle() * 2 + 2 * math.pi * r * h)
    else:
        print("Ошибка, Вы ввели недопустимое значение!")


if __name__ == '__main__':
    cylinder()
