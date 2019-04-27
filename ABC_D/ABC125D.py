# -*- coding: utf-8 -*-
# D - Flipping Signs
# https://atcoder.jp/contests/abc125/tasks/abc125_d

# 時間切れ

n = 3
a = [-10, 5, -4]
b = []

for i in range(n+1):
    print(a[i-1])
    if a[i-1] < 0:
        for j in a:
            calc_a = j * (-1)
            calc_b = j * (-1)
            a.append(calc_a)
            b.append(calc_b)
            print('j：'+str(j))
    else:
        b.append(a[i])

print(b)
print('kotae')
print(sum(b))

# 22:18 - 22:40
