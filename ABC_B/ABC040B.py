# -*- coding: utf-8 -*-
# B - □□□□□
# https://atcoder.jp/contests/abc040/tasks/abc040_b

n = int(input())
ans = 10 ** 9 + 10
num = int(pow(n, 0.5)) + 1

for i in range(1, num):
    width = i
    height = n // width
    mod = n - width * height
    count = abs(width - height) + mod
    if count < ans:
        ans = count

print(ans)

# 15:37 - 17:28（WA）- 17:31（AC）
