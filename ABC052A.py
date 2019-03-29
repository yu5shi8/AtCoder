# -*- coding: utf-8 -*-

a, b, c, d = map(int, input().split())
square1 = a * b
square2 = c * d

if square1 == square2:
    print(square1)
elif square1 > square2:
    print(square1)
else:
    print(square2)

# max を使用すると更にスマート
