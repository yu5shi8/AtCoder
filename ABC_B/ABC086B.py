# -*- coding: utf-8 -*-
# B - 1 21
# https://atcoder.jp/contests/abc086/tasks/abc086_b

ab = int(input().replace(' ',''))

for i in range(1, ab+1):
    n = int(ab // i)
    m = int(ab % i)
    if i == n and m == 0:
        print('Yes')
        exit()
print('No')

# 10:03 - 10:12

# 実はfor文を回さなくても解ける
#   for i in range(1, ab+1):
#       n = int(ab // i)
#       m = int(ab % i)
#       if i == n and m == 0:
# 下記1行でOK
#   if pow(ab, 0.5) % 1 == 0
