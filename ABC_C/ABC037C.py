# -*- coding: utf-8 -*-
# C - 総和
# https://atcoder.jp/contests/abc037/tasks/abc037_c

N, K = map(int, input().split())
a = list(map(int, input().split()))
calc = sum(a[0:K])
ans = calc

for i in range(1, N-K+1):
    calc -= a[i-1]
    calc += a[i+K-1]
    ans += calc

print(ans)

# 14:51 - 15:19（AC）
