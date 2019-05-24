# -*- coding: utf-8 -*-
# D - Handstand
# https://atcoder.jp/contests/abc124/tasks/abc124_d

n, k = map(int, input().split())
s = input()
s += 'X'

ans = 0
l = 0
r = 0
count = 1 if s[0]=='0' else 0

while r < n:
    if count <= k:
        ans = max(ans, r-l+1)
        if s[r]=='1' and s[r+1]=='0':
            count += 1
        r += 1
    else:
        if s[l]=='0' and s[l+1]=='1':
            count -= 1
        l += 1

print(ans)

# 15:41 - 15:49
