# -*- coding: utf-8 -*-
# B - Uneven Numbers
# https://atcoder.jp/contests/abc136/tasks/abc136_b

# 1 から n+1 までを for文で取得する
# len(i) % 2 != 0 の時に count += 1
# count を出力してフィニッシュ

n = int(input())
count = 0

for i in range(1, n + 1):
    if len(str(i)) % 2 != 0:
        count += 1

print(count)

# 14:50 - 14:53（AC）
