# -*- coding: utf-8 -*-
# A - センター採点
# https://atcoder.jp/contests/arc001/tasks/arc001_1

N = int(input())
c = input()

score = {'1':0, '2':0, '3':0, '4':0}

for i in range(N):
    score[c[i]] += 1

print(max(score.values()), min(score.values()))

# 20:21 - 20:26（AC）
