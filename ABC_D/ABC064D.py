# -*- coding: utf-8 -*-
# D - Insertion
# https://atcoder.jp/contests/abc064/tasks/abc064_d

N = int(input())
S = input()

m = 0
min_m = 0

for c in S:
    if c == '(':
        m += 1
    else:
        m -= 1
    min_m = min(min_m, m)

ans = '('*(-min_m) + S + ')'*(m-min_m)
print(ans)

# [1] 16:00 - 16:49（WA）- 22:46（解答を閲覧）
# [2] 22:58 - 23:03（AC）
