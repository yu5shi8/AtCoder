# -*- coding: utf-8 -*-
# A - Sorted Arrays
# https://atcoder.jp/contests/agc013/tasks/agc013_a

N = int(input())
A = list(map(int, input().split()))
count = 1
Flag = None

for i in range(1, N):
    if A[i-1] == A[i]:
        pass
    elif Flag == None:
        Flag = (A[i-1] < A[i])
    elif Flag == (A[i-1] < A[i]):
        pass
    else:
        count += 1
        Flag = None

print(count)

# [1] 10:56 - 11:32（WA）- 12:03（解説を閲覧）/ 15:46 - 16:18（解答を閲覧）
# [2] 17:23 - 17:34（AC）
