# -*- coding: utf-8 -*-
# C - Build Stairs
# https://atcoder.jp/contests/abc136/tasks/abc136_c

n = int(input())
h = list(map(int, input().split()))
check = 0

for i in h:
    if check - 1 <= i:
        check = max(check, i)
    else:
        print('No')
        exit()

print('Yes')

# [1] 14:54 - 15:57（WA）-（解説を閲覧）16:11（WA）-（解答を閲覧）16:22
# [2] 17:32 - 17:35（AC）
