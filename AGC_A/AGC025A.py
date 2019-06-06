# -*- coding: utf-8 -*-
# A - Digits Sum
# https://atcoder.jp/contests/agc025/tasks/agc025_a

n = int(input())

if n % 10 == 0:
    while n > 10:
        n = n // 10
    ans = n
else:
    num = str(n)
    x = 0
    for i in range(len(num)):
        x += int(num[i])
    ans = x

print(ans)

# 15:23 -（解けると思った私が愚かだった）- 16:15（WA）- 16:32（AC）
