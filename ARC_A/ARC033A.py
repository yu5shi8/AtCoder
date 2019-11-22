# -*- coding: utf-8 -*-
# A - 隠れた言葉
# https://atcoder.jp/contests/arc033/tasks/arc033_1

N = int(input())
ans = 0

for i in range(N):
    for j in range(i+1, N+1):
        ans += 1

print(ans)

# 18:52 - 19:18（AC）
