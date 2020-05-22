# -*- coding: utf-8 -*-
# A - The Number of Even Pairs
# https://atcoder.jp/contests/abc159/tasks/abc159_a

N, M = map(int, input().split())

even = 0
for ni in range(N):
    for nj in range(ni, N):
        if ni != nj:
            even += 1

odd = 0
for mi in range(M):
    for mj in range(mi, M):
        if mi != mj:
            odd += 1

ans = even + odd

print(ans)

# 20:39 - 21:00（解説を閲覧） / 22:00 - 22:30（AC）

'''
[コンテスト名] [問題名]、{自力・解説・復習}AC🙌
感想や気付きや学びなど
😄🙂🤯 Difficulty：
😄🙂🤯 Difficulty：○ / Median Solve Time：○分
⏰ 解答時間：○分
https://
'''
