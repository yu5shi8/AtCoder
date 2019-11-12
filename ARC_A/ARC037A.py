# -*- coding: utf-8 -*-
# A - 全優
# https://atcoder.jp/contests/arc037/tasks/arc037_a

N = int(input())
M = list(map(int, input().split()))
b = 80
ans = 0

for m in M:
    if m < b:
        ans += b - m

print(ans)

# 15:12 - 15:13（AC）

'''
[コンテスト名] [問題名]、{自力・解説・復習}AC🙌
感想や気付きや学びなど
😄🙂🤯 Difficulty：
😄🙂🤯 Difficulty：○ / Median Solve Time：○分
⏰ 解答時間：○分
https://
'''
