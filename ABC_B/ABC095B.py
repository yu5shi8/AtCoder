# -*- coding: utf-8 -*-
# B - Bitter Alchemy
# https://atcoder.jp/contests/abc095/tasks/abc095_b

n, x = map(int, input().split())
m = []
ans = 0
for i in range(n):
    m.append(int(input()))
x -= sum(m)
ans += n
while x >= 0:
    x -= min(m)
    ans += 1
print(ans-1)

# 20:21 - 20:45
