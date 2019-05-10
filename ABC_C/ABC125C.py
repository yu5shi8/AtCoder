# -*- coding: utf-8 -*-
# C - GCD on Blackboard
# https://atcoder.jp/contests/abc125/tasks/abc125_c

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

n = int(input())
a = list(map(int, input().split()))

left = [0 for _ in range(n)]
right = [0 for _ in range(n)]
ans = [0 for _ in range(n)]

for i in range(1, n):
    left[i] = gcd(left[i-1], a[i-1])

for i in range(n-2, -1, -1):
    right[i] = gcd(right[i+1], a[i+1])

for i in range(n):
    ans[i] = gcd(left[i], right[i])

print(max(ans))



'''
n = int(input())
a = list(map(int, input().split()))
calc = []
ans = 0

for j in range(n):
    for i in range(1, max(a)):
        if a[j] % i == 0:
            calc.append(i)

calc = sorted(calc)

for i in range(len(calc)):
    if calc.count(calc[i]) == n-1 and ans < calc[i]:
        ans = calc[i]

print(ans)
'''

# 18:36 - 19:36（TLE）
# （解答を閲覧）- 19:45
# 21:21 - 21:40
