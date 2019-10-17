# -*- coding: utf-8 -*-
# A - Kenken Race
# https://atcoder.jp/contests/agc034/tasks/agc034_a

N, A, B, C, D = map(int, input().split())
S = input()
ans = 'Yes'

if '#' in [S[A-1], S[B-1], S[C-1], S[D-1]]:
    ans = 'No'
elif '##' in S[A-1:C] or '##' in S[B-1:D]:
    ans = 'No'
elif A < B and C > D:
    if '...' not in S[B-2:min(C, D)+1]:
        ans = 'No'

print(ans)

# 18:53 - 19:15（3WA）- 19:33（解説・解答を閲覧）- 19:36（AC）
