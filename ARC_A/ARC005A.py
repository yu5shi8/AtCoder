# -*- coding: utf-8 -*-
# A - 大好き高橋君
# https://atcoder.jp/contests/arc005/tasks/arc005_1

N = int(input())
W = list(input().split())
W[-1] = W[-1][:-1]

T = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']
ans = 0

for w in W:
    if w in T:
        ans += 1

print(ans)

# 16:09 - 16:19（AC）
