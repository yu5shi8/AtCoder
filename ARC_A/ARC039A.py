# -*- coding: utf-8 -*-
# A - A - B problem
# https://atcoder.jp/contests/arc039/tasks/arc039_a

A, B = input().split()
ans = []

ans.append(int('9' + A[1:]) - int(B))
ans.append(int(A[:1] + '9' + A[2:]) - int(B))
ans.append(int(A[:2] + '9') - int(B))

ans.append(int(A) - int('1' + B[1:]))
ans.append(int(A) - int(B[:1] + '0' + B[2:]))
ans.append(int(A) - int(B[:2] + '0'))

print(max(ans))

# 13:45 - 13:52（WA）- 14:35（AC）
