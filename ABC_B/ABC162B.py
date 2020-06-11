# -*- coding: utf-8 -*-
# B - FizzBuzz Sum
# https://atcoder.jp/contests/abc162/tasks/abc162_b

N = int(input())
ans = 0

for i in range(1, N+1):
    if i % 3 == 0 and i % 5 == 0:
        ans += 0
    elif i % 3 == 0:
        ans += 0
    elif i % 5 == 0:
        ans += 0
    else:
        ans += i

print(ans)

# 22:10 - 22:13（AC）
