# -*- coding: utf-8 -*-
# C - Poll
# https://atcoder.jp/contests/abc155/tasks/abc155_c

import collections

N = int(input())
S = list(input() for _ in range(N))

c = collections.Counter(S)
cnt = c.most_common()
num = cnt[0][1]

ans = []
for i in range(len(cnt)):
    if num == cnt[i][1]:
        ans.append(cnt[i][0])

ans.sort()
for a in ans:
    print(a)

# 21:11 - 21:32（AC）
