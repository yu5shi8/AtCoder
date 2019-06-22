# -*- coding: utf-8 -*-
# B - Bite Eating
# https://atcoder.jp/contests/abc131/tasks/abc131_b

n, l = map(int, input().split())
taste = [l+i-1 for i in range(1, n+1)]

if 0 in taste:
    ans = sum(taste)
else:
    if min(taste) > 0:
        ans = sum(taste) - min(taste)
    else:
        ans = sum(taste) - max(taste)

print(ans)

# 21:08 - 21:28
