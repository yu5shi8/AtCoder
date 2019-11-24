# -*- coding: utf-8 -*-
# A - ダイナミックなポーズ
# https://atcoder.jp/contests/arc026/tasks/arc026_1

N, A, B = map(int, input().split())

if N >= 5:
    N -= 5
    ans = A * N + B * 5
else:
    ans = B * N

print(ans)

# 19:04 - 19:06（AC）
