# -*- coding: utf-8 -*-
# C - Make a Rectangle
# https://atcoder.jp/contests/abc071/tasks/arc081_a

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
a = 0
b = 0
check = False

for i in range(1, N):
    if check == True:
        check = False
        pass
    else:
        if A[i-1] == A[i]:
            if a == 0:
                a = A[i]
            elif b == 0:
                b = A[i]
                print(a * b)
                exit()
            check = True

print(0)

# 22:48 - 23:05（AC）
