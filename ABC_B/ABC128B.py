# -*- coding: utf-8 -*-
# B - Guidebook
# https://atcoder.jp/contests/abc128/tasks/abc128_b

n = int(input())
sp = [list(input().split()) for _ in range(n)]
ans = [0]*n

for i in range(1, n+1):
    sp[i-1][1] = int(sp[i-1][1])
    sp[i-1].append(i)

sp = sorted(sp, key=lambda x:(x[0],-x[1]))

for i in range(n):
    ans[i] += sp[i][2]

print(*ans, sep='\n')

# 21:05 - 21:40
# 21:58 - 22:40（時間切れ）
# 22:43（AC）
