# -*- coding: utf-8 -*-
# B - Palace
# https://atcoder.jp/contests/abc113/tasks/abc113_b

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
temp = [0]*n
ans = [0]*n

for i in range(n):
    temp[i] = t - h[i] * 0.006
    ans[i] = abs(temp[i] - a)

print(ans.index(min(ans))+1)

# 17:02 - 17:10
