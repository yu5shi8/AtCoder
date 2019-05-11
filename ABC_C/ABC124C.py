# -*- coding: utf-8 -*-
# C - Coloring Colorfully
# https://atcoder.jp/contests/abc124/tasks/abc124_c

s = list(map(int, input()))
ans = 0

for i in range(len(s)):
    if i % 2 == s[i]:
        ans += 1

print(min(ans, len(s)-ans))

# 14:40 - 15:00
# （解説を聞いた）16:54 - 17:56
