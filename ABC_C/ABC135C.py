# -*- coding: utf-8 -*-
# C - City Savers
# https://atcoder.jp/contests/abc135/tasks/abc135_c

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []

for i in range(1, n + 1):
    if a[i - 1] <= b[i - 1]:
        ans.append(a[i - 1])
        b[i - 1] = b[i - 1] - a[i - 1]
        a[i - 1] = 0
        if a[i] >= b[i - 1]:
            ans.append(b[i - 1])
            a[i] = a[i] - b[i - 1]
            b[i - 1] = 0
        else:
            ans.append(a[i])
            b[i - 1] = b[i - 1] - a[i]
            a[i] = 0
    else:
        ans.append(b[i - 1])
        a[i - 1] = a[i - 1] - b[i - 1]
        b[i - 1] = 0

print(sum(ans))

# 21:15 - 21:50（WA）-（解説を閲覧）-（解答を閲覧）23:10
# 19:53 - 20:14（AC）
