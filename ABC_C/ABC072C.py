# -*- coding: utf-8 -*-
# C - Together
# https://atcoder.jp/contests/abc072/tasks/arc082_a

import collections

n = int(input())
a = list(map(int, input().split()))

plus = []
minus = []

for i in a:
    minus.append(i-1)
    plus.append(i+1)

all_l = a + minus + plus
ans = collections.Counter(all_l)
print(ans.most_common(1)[0][1])

# 18:50 - 19:33
# 16:19 - 17:19
# 17:42 - 18:20（TLE）- 18:31（AC）
