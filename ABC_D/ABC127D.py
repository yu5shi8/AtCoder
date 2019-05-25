# -*- coding: utf-8 -*-
# D - Integer Cards
# https://atcoder.jp/contests/abc127/tasks/abc127_d

n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = sorted([list(map(int, input().split())) for _ in range(m)])
print(bc)

count = 0
num = [0]*n
ans = 0

for i in range(m):
    print('i：'+str(i))
    if sum(bc[i]) > ans:
        ans = sum(bc[i])
    count = 0
    num[i] = a[i]
    if num[i] < bc[i][1] and count < m:
        num[i] = bc[i][1]
        calc = sum(bc[i])
        count += 1
    print(num)

print(ans)

# 22:20 - 22:40（時間切れ）
