# -*- coding: utf-8 -*-
# C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c

abcd = input()
n = 3

for i in range(2**n):
    num = []
    bi = format(i, '03b')
    for j in range(n):
        num.append(abcd[j])
        if bi[j] == '0':
            num.append('+')
        else:
            num.append('-')
    num.append(abcd[-1])
    calc = ''.join(num)
    if eval(calc) == 7:
        break

print(str(calc)+'=7')

# 21:49 - 22:00
