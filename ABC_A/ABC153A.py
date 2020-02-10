# -*- coding: utf-8 -*-
# A - Serval vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_a

H, A = map(int, input().split())

ans = H // A
if H % A != 0:
    ans += 1

print(ans)

# 21:00 - 21:01（AC）
