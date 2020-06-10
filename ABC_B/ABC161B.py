# -*- coding: utf-8 -*-
# B - Popular Vote
# https://atcoder.jp/contests/abc161/tasks/abc161_b

N, M = map(int, input().split())
A = list(map(int, input().split()))

all_A = sum(A)
border = all_A / (M*4)

select = 0

for a in A:
    if a >= border:
        select += 1

if select >= M:
    print('Yes')
else:
    print('No')

# 21:51 - 21:56（おふろ）/ 22:51 - 22:55（WA）- 22:57（WA）- 22:58（WA）- 23:02（WA）- 23:07（WA）- 23:17（WA）- 23:21（解説AC）
