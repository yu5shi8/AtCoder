# -*- coding: utf-8 -*-
# B - Time Limit Exceeded
# https://atcoder.jp/contests/abc112/tasks/abc112_b

n, t = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(n)]
ans = []

for i in ct:
    if i[1] <= t:
        ans.append(i)

if not ans:
    print('TLE')
else:
    ans.sort(key=lambda x: x[0])
    print(ans[0][0])

# 15:59 - 16:09
