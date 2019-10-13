# -*- coding: utf-8 -*-
# C - Digits in Multiplication
# https://atcoder.jp/contests/abc057/tasks/abc057_c

N = int(input())

def check_digit(n):
    cnt = 0
    while n > 0:
        n //= 10
        cnt += 1
    return cnt

ans = 10**9 + 7
for i in range(1, int(N**0.5//1)+1):
    if N % i == 0:
        a = i
        b = N // i
        ans = min(ans, max(check_digit(a), check_digit(b)))

print(ans)

# [1] 21:01 - 21:20（WA / 解説を閲覧）21:29 -（解答を閲覧）- 21:37
# [2] 21:42 - 21:44（AC）
