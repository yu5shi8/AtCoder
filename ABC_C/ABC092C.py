# -*- coding: utf-8 -*-
# C - Traveling Plan
# https://atcoder.jp/contests/abc092/tasks/arc093_a

n = int(input())
a = list(map(int, input().split())) + [0]
b = [abs(a[0])]
c = [abs(a[1])]

for i in range(n):
    b.append(abs(a[i] - a[i + 1]))
    if i < n - 1:
        c.append(abs(a[i] - a[i + 2]))

sum_b = sum(b)
for i in range(n):
    print(sum_b + c[i] - b[i] - b[i + 1])

# [1] 17:33 - 18:28（WA）- 13:32 -（解説・解答を閲覧）- 14:46
# [2] 15:00 - 15:09（AC）
