# -*- coding: utf-8 -*-
# C - Special Trains
# https://atcoder.jp/contests/abc084/tasks/abc084_c

N = int(input())
csf = [list(map(int, input().split())) for _ in range(N-1)]
ans = []

for i in range(N):
    t = 0
    for j in range(i, N-1):
        C = csf[j][0]
        S = csf[j][1]
        F = csf[j][2]
        if S <= t:
            if t % F == 0:
                t += C
            else:
                t += F - t % F + C
        else:
            t = C + S
    ans.append(t)

print(*ans, sep='\n')

# [1] 13:59 - 16:14（WA / 解説を閲覧）16:29（解答を閲覧）- 16:45
# [2] 18:05 - 18:45（AC）
