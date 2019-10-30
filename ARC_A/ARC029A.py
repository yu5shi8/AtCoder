# -*- coding: utf-8 -*-
# A - 高橋君とお肉
# https://atcoder.jp/contests/arc029/tasks/arc029_1

N = int(input())
t = [int(input()) for _ in range(N)]
total = sum(t)
ans = total

if N == 1:
    print(t[0])
    exit()

for i in range(2**N):
    bbq = []
    for j in range(N):
        if ((i >> j) & 1):
            bbq.append(t[j])
    A = sum(bbq)
    B = total - A
    num = abs(A - B)
    if ans > num:
        ans = num
        ans_A = A
        ans_B = B

print(max(ans_A, ans_B))

# 15:06 - 16:10（AC）
