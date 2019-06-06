# -*- coding: utf-8 -*-
# A - 豆まき
# https://atcoder.jp/contests/abc018/tasks/abc018_1

a = [1] + [int(input())]
b = [2] + [int(input())]
c = [3] + [int(input())]

rank = [a, b, c]
rank.sort(key=lambda x:-x[1])
for i in range(3):
    rank[i].append(i+1)
rank.sort(key=lambda x:x[0])

for i in range(3):
    print(rank[i][2])

# 10:09 - 10:18
