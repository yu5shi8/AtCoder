# -*- coding: utf-8 -*-
# C - Traveling
# https://atcoder.jp/contests/abc086/tasks/arc089_a

N = int(input())
T = [0]
X = [0]
Y = [0]

for i in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

for i in range(1, N+1):
    if abs(T[i-1] - T[i]) < abs(X[i-1] - X[i]) + abs(Y[i-1] - Y[i]):
        print('No')
        exit()
    else:
        if T[i] % 2 != 0 and (X[i]+Y[i]) % 2 == 0:
            print('No')
            exit()
        elif T[i] % 2 == 0 and (X[i]+Y[i]) % 2 != 0:
            print('No')
            exit()

print('Yes')

# 13:41 - 14:18（AC）
