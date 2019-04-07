# -*- coding: utf-8 -*-
# A - Five Antennas
# https://atcoder.jp/contests/abc123/tasks/abc123_a

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

ab = abs(a - b)
ac = abs(a - c)
ad = abs(a - d)
ae = abs(a - e)
bc = abs(b - c)
bd = abs(b - d)
be = abs(b - e)
cd = abs(c - d)
de = abs(d - e)

if ab > k or ac > k or ad > k or ae > k or bc > k or bd > k or be > k or cd > k or de > k:
    print(':(')
else:
    print('Yay!')

# 総当たりしなくても、A〜Eの距離とKを調べればOKだった…
# if abs(e - a) > k:
#     print(':(')
# else:
#     print('Yay!')
