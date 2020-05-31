# -*- coding: utf-8 -*-
# B - Multiplication 2 / 
# https://atcoder.jp/contests/abc169/tasks/abc169_b

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 1
check = 10 ** 18

for i in range(N):
    num = A[i]
    ans *= num
    if ans > check:
        ans = -1
        break
    elif ans == 0:
        break

print(ans)

# 21:00 - 21:09（WA）- 21:19（WA）- 21:20（WA）- 21:22（TLE）- 21:43（AC）
