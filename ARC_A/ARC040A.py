# -*- coding: utf-8 -*-
# A - 床塗り
# https://atcoder.jp/contests/arc040/tasks/arc040_a

N = int(input())
S = [input() for _ in range(N)]

game = {'R':0, 'B':0, '.':0}

for i in range(N):
    for j in range(N):
        game[S[i][j]] += 1

if game['R'] > game['B']:
    print('TAKAHASHI')
elif game['R'] < game['B']:
    print('AOKI')
else:
    print('DRAW')

# 17:23 - 17:30（WA） - 17:31（WA）- 17:34（WA）- 17:40（AC）
