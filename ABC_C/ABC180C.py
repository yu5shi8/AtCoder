# -*- coding: utf-8 -*-
# C - Cream puff
# https://atcoder.jp/contests/abc180/tasks/abc180_c

N = int(input())

def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n//i)
    return_list.sort()
    return return_list

ans = make_divisors(N)

for i in ans:
    print(i)

# 20:17 - 20:21（AC）
