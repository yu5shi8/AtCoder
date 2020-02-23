# -*- coding: utf-8 -*-
# B - Count ABC
# https://atcoder.jp/contests/abc150/tasks/abc150_b

N = int(input())
s = input()
cnt = 0

for i in range(3, N+1):
    if s[i-3:i] == 'ABC':
        cnt += 1

print(cnt)

# - 23:00（AC）
