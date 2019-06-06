# -*- coding: utf-8 -*-
# A - 足し算
# https://atcoder.jp/contests/abc021/tasks/abc021_a

n = int(input())
count = 0
ans = []

while n > 0:
    if n - 8 >= 0:
        n -= 8
        count += 1
        ans.append(8)
    elif n - 4 >= 0:
        n -= 4
        count += 1
        ans.append(4)
    elif n - 2 >= 0:
        n -= 2
        count += 1
        ans.append(2)
    else:
        n -= 1
        count += 1
        ans.append(1)

print(count)
print(*ans, sep='\n')

# 9:51 - 9:57
