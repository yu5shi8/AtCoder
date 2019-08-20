# -*- coding: utf-8 -*-
# B - 手芸王
# https://atcoder.jp/contests/abc023/tasks/abc023_b

n = int(input())
s = input()
cnt = 0

if n % 2 != 0 and s[n // 2] == 'b':
    cnt += 0
else:
    print(-1)
    exit()

for i in range(n // 2):
    if s[i] == 'a' and s[n - i -1] == 'c':
        cnt += 1
    elif s[i] == 'c' and s[n - i -1] == 'a':
        cnt += 1
    elif s[i] == 'b' and s[n - i -1] == 'b':
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)

# 15:31 - 15:50（AC）
