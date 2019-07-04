# -*- coding: utf-8 -*-
# C - Candies
# https://atcoder.jp/contests/abc087/tasks/arc090_a

n = int(input())
a_1 = list(map(int, input().split()))
a_2 = list(map(int, input().split()))
ans = 0

for i in range(n):
    to_right = sum(a_1[:i+1])
    to_left = sum(a_2[i:])
    calc = to_right + to_left
    if calc > ans:
        ans = calc

print(ans)

# 14:58 - 15:12（AC）
