# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def composition():
    n = 1
    print("Признак окончания: '0'")
    while True:
        a = int(input("Введите число: "))
        if a == 0:
            return print(f"Произведение чисел: {n}")
        else:
            n *= a


if __name__ == '__main__':
    composition()
