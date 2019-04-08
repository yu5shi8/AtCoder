# -*- coding: utf-8 -*-
# A - AtCoder Beginner Contest 999
# https://atcoder.jp/contests/abc111/tasks/abc111_a
'''
n = int(input())

if n % 10 >= 9:
    n -= 8
else:
    n += 8

if n % 100 >= 90:
    n -= 80
else:
    n += 80

if n >= 900:
    n -= 800
else:
    n += 800

print(n)
'''

n = input()
ans = n.replace('1', 'x').replace('9', '1').replace('x', '9')
print(ans)
