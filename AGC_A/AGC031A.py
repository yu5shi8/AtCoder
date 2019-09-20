# -*- coding: utf-8 -*-
# A - Colorful Subsequence
# https://atcoder.jp/contests/agc031/tasks/agc031_a

N = int(input())
S = input()
mod = 10**9 + 7

S_dict = {}
for s in S:
    if s not in S_dict:
        S_dict[s] = 1
    else:
        S_dict[s] += 1

ans = 1
for v in S_dict.values():
    ans *= (v + 1)
    ans %= mod

print(ans - 1)

# [1] 9:14 - 9:44 / 13:56 - 14:28（解説・解答を閲覧）14:39
# [2] 10:18 -（解説を閲覧）10:37（AC）
