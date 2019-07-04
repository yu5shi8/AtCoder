# -*- coding: utf-8 -*-
# B - 視程の通報
# https://atcoder.jp/contests/abc001/tasks/abc001_2

m = int(input())

if m < 100:
    vv = '00'
elif 100 <= m <= 5000:
    vv = m // 100
    if len(str(vv)) == 1:
        vv = '0' + str(vv)
elif 6000 <= m <= 30000:
    vv = m // 1000 + 50
elif 35000 <= m <= 70000:
    vv = (m // 1000 - 30) // 5 + 80
else:
    vv = 89

print(vv)

# 14:47 - 14:55（AC）
