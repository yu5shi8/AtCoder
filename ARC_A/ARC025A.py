# -*- coding: utf-8 -*-
# A - ゴールドラッシュ
# https://atcoder.jp/contests/arc025/tasks/arc025_1

D = list(map(int, input().split()))
J = list(map(int, input().split()))
ans = 0

for i in range(7):
    if D[i] >= J[i]:
        ans += D[i]
    else:
        ans += J[i]

print(ans)

# 17:59 - 18:03（AC）
