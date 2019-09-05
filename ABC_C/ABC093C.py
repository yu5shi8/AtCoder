# -*- coding: utf-8 -*-
# C - Same Integers
# https://atcoder.jp/contests/abc093/tasks/arc094_a

A, B, C = map(int, input().split())
L = [A, B, C]
even = []
odd = []
ans = 0

for i in L:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(even) == 2:
    even[0] += 1
    even[1] += 1
    ans += 1
    num = even + odd
elif len(odd) == 2:
    odd[0] += 1
    odd[1] += 1
    ans += 1
    num = even + odd
else:
    num = L

num.sort()
ans_1 = (num[1] - num[0]) // 2
ans_2 = num[2] - num[1]
ans += ans_1 + ans_2
print(ans)

# 16:35 - 17:08（AC）
