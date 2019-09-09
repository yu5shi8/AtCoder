# -*- coding: utf-8 -*-
# A - A+...+B Problem
# https://atcoder.jp/contests/agc015/tasks/agc015_a

N, A, B = map(int, input().split())

if N == 1 and A == B:
    print(1)
    exit()
elif N == A == B:
    print(1)
    exit()

if A >= B:
    print(0)
    exit()
elif N == 1 and A != B:
    print(0)
    exit()

digit = N - 1
min_calc = A*digit + B
max_calc = A + B*digit
ans = max_calc - min_calc + 1
print(ans)

# 11:33 - 12:15 / 13:33 - 13:43（WA）- 13:47（WA）-（テストケースを閲覧）13:52（AC）
