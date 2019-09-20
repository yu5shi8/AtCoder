# -*- coding: utf-8 -*-
# A - Shik and Stone
# https://atcoder.jp/contests/agc007/tasks/agc007_a

H, W = map(int, input().split())
A = [input() for _ in range(H)]

prev_left = 0
prev_right = 0

for i in range(H):
    left = A[i].find('#')
    right = A[i].rfind('#')
    if prev_right == left:
        prev_left = left
        prev_right = right
    elif right == W-1:
        right = W
        break
    elif prev_left == left and prev_right == right:
        break

if right == W-1:
    print('Possible')
else:
    print('Impossible')

# 10:58 - 11:20（WA）/ 9:12 - 9:36（WA）- 9:44（AC）
