# -*- coding: utf-8 -*-
# A - ドミノ色塗り
# https://atcoder.jp/contests/arc053/tasks/arc053_a

H, W = map(int, input().split())

if H == 1 and W == 1:
    ans = 0
elif H == 1:
    ans = W - 1
elif W == 1:
    ans = H - 1
else:
    ans = (H-1)*W + (W-1)*H

print(ans)

# 18:06 - 18:13（AC）
