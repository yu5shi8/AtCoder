# -*- coding: utf-8 -*-
# C - Boxes and Candies
# https://atcoder.jp/contests/abc048/tasks/arc064_a

N, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(1, N):
    calc = max(0, a[i-1] + a[i] - x)
    ans += calc
    a[i] = max(0, a[i] - calc)

print(ans)

# 13:32 - 13:58（WA）- 14:12（AC）
