# -*- coding: utf-8 -*-
# B - Papers, Please
# https://atcoder.jp/contests/abc155/tasks/abc155_b

N = int(input())
A = list(map(int, input().split()))

even = []

for a in A:
    if a % 2 == 0:
        even.append(a)

ans = []
for e in even:
    if e % 5 == 0:
        ans.append(e)
    elif e % 3 == 0:
        ans.append(e)

if even == ans:
    print('APPROVED')
else:
    print('DENIED')

# 21:04 - 21:09（AC）
