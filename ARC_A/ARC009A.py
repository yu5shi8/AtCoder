# -*- coding: utf-8 -*-
# A - 元気にお使い！高橋君
# https://atcoder.jp/contests/arc009/tasks/arc009_1

N = int(input())
money = 0

for i in range(N):
    a, b = map(int, input().split())
    money += a * b

ans = int(money * 1.05)
print(ans)

# 10:51 - 10:54（AC）
