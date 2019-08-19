# -*- coding: utf-8 -*-
# B - 高橋くんと文字列圧縮
# https://atcoder.jp/contests/abc019/tasks/abc019_2

s = input()
j = 0
count = 0
ans = ''

for i in range(len(s)):
    if s[j] == s[i]:
        count += 1
    elif i == len(s) - 1 or s[j] != s[i]:
        ans += str(s[j]) + str(count)
        j = i
        count = 1

ans += str(s[-1]) + str(count)
print(ans)

# 17:03 - 17:32（AC）
