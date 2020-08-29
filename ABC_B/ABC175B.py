# -*- coding: utf-8 -*-
# B - Making Triangle
# https://atcoder.jp/contests/abc175/tasks/abc175_b

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0

for i in range(N):
    for j in range(i):
        for k in range(j):
            if L[i] != L[j] and L[j] != L[k]:
                if L[j] + L[k] > L[i]:
                    ans += 1

print(ans)

# 15:29 - 16:03（解説を閲覧）- 16:23（C++を翻訳写経）
# 17:02 - 17:10（AC）
