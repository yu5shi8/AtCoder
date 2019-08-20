# -*- coding: utf-8 -*-
# B - 自動ドア
# https://atcoder.jp/contests/abc024/tasks/abc024_b

n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
num = a[0] + t
ans = 0

for i in range(1, n):
    if num < a[i]:
        ans += t
    else:
        ans += a[i] - a[i - 1]
    num = a[i] + t

print(ans + t)

# 15:59 - 16:12（AC）
