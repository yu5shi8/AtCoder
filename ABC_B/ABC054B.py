# -*- coding: utf-8 -*-
# B - Template Matching
# https://atcoder.jp/contests/abc054/tasks/abc054_b

n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for i in range(n-m+1):
    for j in range(n-m+1):
        for k in range(m):
            Flag = True
            if a[i+k][j:j+m] != b[k]:
                Flag = False
                break
        if Flag == True:
            print('Yes')
            exit()

print('No')

# [1] 15:04 -（解説・解答を閲覧）16:40 - 16:44
# [2] 16:52 - 17:01
