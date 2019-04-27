# -*- coding: utf-8 -*-
# C - GCD on Blackboard
# https://atcoder.jp/contests/abc125/tasks/abc125_c

# 時間切れ

n = int(input())
a = list(map(int, input().split()))
count = []
sorted(count, reverse=True)
ans = []

for i in range(n):
    print('---')
    print(a[i])
    for j in range(1, 100):
        print(j)
        if a[i] % j == 0:
            count.append(a[i] // j)

count = sorted(count, reverse=True)
print(count)

print('---\nここから最大公約数の検討')

for i in count:
    print(i)
    if count(i-1) == count(i):
        ans.append(i)

print(ans)
print(max(ans))


# 21:25 - 22:18
