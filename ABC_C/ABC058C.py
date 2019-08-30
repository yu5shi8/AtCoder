# -*- coding: utf-8 -*-
# C - 怪文書 / Dubious Document
# https://atcoder.jp/contests/abc058/tasks/arc071_a

import string

n = int(input())
s = [input() for _ in range(n)]
l = string.ascii_lowercase
ans = ''

for i in l:
    ans += i * min(j.count(i) for j in s)

print(ans)

# 9:35 - 9:57（WA）- 10:10（WA）- 10:12（WA）-（解答を閲覧）10:21（AC）
