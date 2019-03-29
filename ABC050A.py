# -*- coding: utf-8 -*-
# A - Addition and Subtraction Easy
# https://atcoder.jp/contests/abc050/tasks/abc050_a

a, op, b = input().split()
a = int(a)
b = int(b)

if op == '+':
    calc = a + b
elif op == '-':
    calc = a - b

print(calc)

# eval 使えば、第1引数を式として評価してくれるので、よりスマート
