# -*- coding: utf-8 -*-
# C - Skip
# https://atcoder.jp/contests/abc109/tasks/abc109_c

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, X = map(int, input().split())
x = list(map(int, input().split())) + [X]
D = [0] * N

for i in range(N):
    D[i] = abs(X - x[i])

if N == 1:
    print(D[0])
    exit()

ans = gcd(D[0], D[1])
for j in range(2, N):
    ans = gcd(ans, D[j])

print(ans)

# 18:42 - 18:57（WA）- 19:48（WA）- 20:02（WA）
#（解説を閲覧）- 21:05 - （解答を閲覧）21:12（WA）- 21:16（AC）
