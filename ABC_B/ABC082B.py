# # -*- coding: utf-8 -*-
# B - Two Anagrams
# https://atcoder.jp/contests/abc082/tasks/abc082_b

s = sorted(input())
t = sorted(input(), reverse=True)

if s < t:
    print('Yes')
else:
    print('No')

# 19:04 - 19:16
# 15:30 - 15:53【解説】
