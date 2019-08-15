# -*- coding: utf-8 -*-
# B - 投票
# https://atcoder.jp/contests/abc008/tasks/abc008_2

n = int(input())
vote = {}

for i in range(n):
    name = input()
    if name in vote:
        vote[name] += 1
    else:
        vote.setdefault(name, 1)

print(max(vote.items(), key=lambda x:x[1])[0])

# 21:40 - 21:50（AC）
