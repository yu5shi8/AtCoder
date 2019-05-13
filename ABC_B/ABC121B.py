# -*- coding: utf-8 -*-
# B - Can you solve this?
# https://atcoder.jp/contests/abc121/tasks/abc121_b

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range (n)]
ans = 0

for i in range(n):
    calc = 0
    for j in range(m):
        calc += a[i][j]*b[j]
    if calc + c > 0:
        ans += 1

print(ans)

# 20:29 - 20:45
# 21:05 - 21:12
