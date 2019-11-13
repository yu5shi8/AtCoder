# -*- coding: utf-8 -*-
# A - みんなでワイワイみかん
# https://atcoder.jp/contests/arc056/tasks/arc056_a

A, B, K, L = map(int, input().split())

a_price = A * L
b_price = B

if a_price <= b_price:
    ans = A * K
else:
    num = K // L
    ans = B * num
    if K % L != 0:
        a = K % L
    else:
        a = 0
    ans += min(A*a, B)

print(ans)

# 15:01 - 15:23（AC）
