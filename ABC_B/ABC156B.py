# -*- coding: utf-8 -*-
# B - Digits
# https://atcoder.jp/contests/abc156/tasks/abc156_b

N, K = map(int, input().split())
cnt = 0

while N // K > 0:
    N //= K
    cnt += 1

if N >= 1:
    cnt += 1

print(cnt)

# 19:31 - 19:36（AC）

'''
[コンテスト名] [問題名]、{自力・解説・復習}AC🙌
感想や気付きや学びなど
😄🙂🤯 Difficulty：
😄🙂🤯 Difficulty：○ / Median Solve Time：○分
⏰ 解答時間：○分
https://
'''
