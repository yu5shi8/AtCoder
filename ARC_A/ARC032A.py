# -*- coding: utf-8 -*-
# A - ホリドッグ
# https://atcoder.jp/contests/arc032/tasks/arc032_1

n = int(input())
num = sum([i for i in range(1, n+1)])
ans = 'WANWAN'

if num == 1:
    ans = 'BOWWOW'
else:
    for i in range(2, num):
        if num % i == 0:
            ans = 'BOWWOW'
            break

print(ans)

# 17:17 - 17:25（AC）
