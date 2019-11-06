# -*- coding: utf-8 -*-
# B - 迷子のCDケース
# https://atcoder.jp/contests/arc007/tasks/arc007_2

N, M = map(int, input().split())
d = [int(input()) for _ in range(M)]
case = [i for i in range(1, N+1)]

if M == 0:
    print(*case, sep='\n')
    exit()

disc = d[0]
if disc != 0:
    case[d[0]-1] = 0

for i in range(1, M):
    if d[i-1] == d[i]:
        pass
    else:
        disc, playing = d[i], d[i-1]
        n = case.index(disc)
        case[n] = playing

print(*case, sep='\n')

# 16:13 - 16:33（AC）
