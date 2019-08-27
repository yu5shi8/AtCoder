# -*- coding: utf-8 -*-
# C - Good Sequence
# https://atcoder.jp/contests/abc082/tasks/arc087_a

n = int(input())
a = list(map(int, input().split()))
dic_a = {}

for i in a:
    if i not in dic_a:
        dic_a[i] = 1
    else:
        dic_a[i] += 1

dic_a = dic_a.items()
ans = 0

for j in dic_a:
    if j[0] <= j[1]:
        ans += j[1] - j[0]
    elif j[0] > j[1]:
        ans += j[1]

print(ans)

# 16:42 - 16:52（WA）- 17:07（WA）-（解説・解答を閲覧）17:17（AC）
