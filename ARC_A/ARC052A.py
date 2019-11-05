# -*- coding: utf-8 -*-
# A - 何期生？
# https://atcoder.jp/contests/arc052/tasks/arc052_a

S = input()
num = [str(i) for i in range(0, 10)]
ans = ''

for i in S:
    if i in num:
        ans += i

print(ans)

# 20:28 - 20:33（AC）
