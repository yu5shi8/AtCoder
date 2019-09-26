# -*- coding: utf-8 -*-
# C - こだわり者いろはちゃん / Iroha's Obsession
# https://atcoder.jp/contests/abc042/tasks/arc058_a

N, K = map(int, input().split())
D = set(input().split())

for i in range(N, 10**5):
    if set(str(i)) & D == set():
        print(i)
        exit()

# [1] 15:03 - 15:50（解説・解答を閲覧 / no_sub）
# [2] 17:00 - 17:31（解説・解答を閲覧 / WA）
# [3] 10:43 - 10:49（AC）
