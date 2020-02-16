# -*- coding: utf-8 -*-
# A - Poor
# https://atcoder.jp/contests/abc155/tasks/abc155_a

ABC = list(map(int, input().split()))
ABC.sort()

if ABC[0] == ABC[1] != ABC[2]:
    print('Yes')
elif ABC[0] != ABC[1] == ABC[2]:
    print('Yes')
else:
    print('No')

# 21:00 - 21:02（WA） - 21:03（AC）
