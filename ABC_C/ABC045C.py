# -*- coding: utf-8 -*-
# C - たくさんの数式 / Many Formulas
# https://atcoder.jp/contests/abc045/tasks/arc061_a

s = input()
n = len(s) - 1
ans = 0

for i in range(2**n):
    num = []
    bi = format(i, '0'+str(n)+'b')
    for j in range(n):
        num.append(s[j])
        if bi[j] == '1':
            num.append('+')
    num.append(s[-1])
    calc = ''.join(num)
    ans += eval(calc)

print(ans)

# 18:13 - 21:33
# 21:40 - 21:45
