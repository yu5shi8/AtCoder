# -*- coding: utf-8 -*-
# B - Mix Juice
# https://atcoder.jp/contests/abc171/tasks/abc171_b

N, K = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

ans = sum(p[:K])
print(ans)

# 21:02 - 21:04（AC）
