# -*- coding: utf-8 -*-
# D - Disjoint Set of Common Divisors
# https://atcoder.jp/contests/abc142/tasks/abc142_d

def prime_factorize(n):
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            pf.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        pf.append(n)
    return pf

A, B = map(int, input().split())

prime_A = set(prime_factorize(A))
prime_B = set(prime_factorize(B))
ans = len(prime_A & prime_B) + 1

print(ans)

# 21:21 - 22:02（TLE）- 22:20（TLE / わかりません）
# 素因数分解？ と粘ったけれど、結局わかりませんでした…
# 22:49 - 23:20（RE）- 23:38（WA）
# 18:03（AC）
