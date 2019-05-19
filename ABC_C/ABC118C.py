# -*- coding: utf-8 -*-
# C - Monsters Battle Royale
# https://atcoder.jp/contests/abc118/tasks/abc118_c

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

n = int(input())
a = list(map(int, input().split()))
num = 0

for i in range(n):
    num = gcd(num, a[i])

print(num)


'''
# WA
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

comp = [10**9] * n
max_hp = a[n-1]

for i in range(1, n):
    if a[i] % a[i-1] == 0:
        comp[i-1] = a[i-1]
    else:
        comp[i-1] = a[i] % a[i-1]

min_attack = min(comp)
ans = min(min_attack, max_hp%min_attack if max_hp%min_attack!=0 else max_hp)

print(ans)
'''

# 11:06 - 12:28（WA）
# （解説・解答を閲覧）- 12:52
