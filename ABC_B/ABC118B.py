# -*- coding: utf-8 -*-
# B - Foods Loved by Everyone
# https://atcoder.jp/contests/abc118/tasks/abc118_b

n, m = map(int, input().split())
ka = [list(map(int, input().split())) for _ in range(n)]
ans = [0]*m

for i in range(n):
    for j in ka[i][1:]:
        ans[j-1] += 1

print(ans.count(n))

# 10:58 - 11:05
