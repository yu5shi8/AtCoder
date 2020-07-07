# -*- coding: utf-8 -*-
# B - 1%
# https://atcoder.jp/contests/abc165/tasks/abc165_b

X = int(input())
M = 100
ans = 0

while X > M:
    tax = M // 100
    M += tax
    ans += 1

print(ans)

# 17:26 - 17:40（WA）- 17:56（他の解答を閲覧してAC）
# 21:19 - 21:22（AC）
