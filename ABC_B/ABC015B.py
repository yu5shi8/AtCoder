# -*- coding: utf-8 -*-
# B - 高橋くんの集計
# https://atcoder.jp/contests/abc015/tasks/abc015_2

n = int(input())
a = list(map(int, input().split()))
num = 0

for i in range(n):
    if a[i] != 0:
        num += 1

ans = sum(a) // num

if sum(a) % num > 0:
    ans += 1

print(ans)

# 9:53 - 9:58（AC）
