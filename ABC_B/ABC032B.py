# -*- coding: utf-8 -*-
# B - 高橋君とパスワード
# https://atcoder.jp/contests/abc032/tasks/abc032_b

s = input()
k = int(input())
ans = []

for i in range(len(s)):
    if s[i:i+k] not in ans and len(s[i:i+k]) == k:
        ans.append(s[i:i+k])

print(len(ans))

# 15:21 - 15:27（AC）
