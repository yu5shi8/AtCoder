# -*- coding: utf-8 -*-
# B - Snake Toy
# https://atcoder.jp/contests/abc067/tasks/abc067_b

n, k = map(int, input().split())
l = list(map(int, input().split()))

l = sorted(l, reverse=True)
ans = sum(l[0:k])

print(ans)

# 22:16 - 22:21
