# -*- coding: utf-8 -*-
# B - Break Number
# https://atcoder.jp/contests/abc068/tasks/abc068_b

n = int(input())
count = 0
ans = n

for i in range(n, 0, -1):
    cnt = 0
    j = i
    while j % 2 == 0:
        j //= 2
        cnt += 1
        if count < cnt:
            count = cnt
            ans = i

print(ans)

# 21:31 - 22:08
