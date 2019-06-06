# -*- coding: utf-8 -*-
# C - /\/\/\/
# https://atcoder.jp/contests/abc111/tasks/arc103_a

import collections

n = int(input())
v = list(map(int, input().split()))

odd_l = []
even_l = []

if v.count(v[0]) == n:
    ans = n // 2
else:
    for i in range(0, n, 2):
        odd_l.append(v[i])
        even_l.append(v[i+1])

    odd_c = collections.Counter(odd_l)
    even_c = collections.Counter(even_l)

    odd = odd_c.most_common()[0][1]
    odd_num = odd_c.most_common()[0][0]

    even = even_c.most_common()[0][1]
    even_num = even_c.most_common()[0][0]

    if odd_num != even_num:
        ans = n - (odd + even)
    else:
        odd = odd_c.most_common()[1][1]
        even = even_c.most_common()[0][1]
        ans_change_odd = n - (odd + even)

        odd = odd_c.most_common()[0][1]
        even = even_c.most_common()[1][1]
        ans_change_even  = n - (odd + even)

        ans = min(ans_change_odd, ans_change_even)

print(ans)

# 11:40 - 12:10
# 14:23 - 14:35（WA）
# 15:09（AC）
