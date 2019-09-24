# -*- coding: utf-8 -*-
# A - Airport Bus
# https://atcoder.jp/contests/agc011/tasks/agc011_a

N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

bus = [T[0]]
count = 1

for i in range(1, N):
    if T[i] <= bus[0] + K and len(bus) < C:
        bus.append(T[i])
    else:
        count += 1
        bus = []
        bus.append(T[i])

print(count)

# [1] 15:54 - 16:29（RE）/（解説・解答を閲覧）
# [2] 17:38 - 17:46（AC）
