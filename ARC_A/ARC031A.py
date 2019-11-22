# -*- coding: utf-8 -*-
# A - 名前
# https://atcoder.jp/contests/arc031/tasks/arc031_1

Name = input()
check = Name[::-1]

if Name == check:
    print('YES')
else:
    print('NO')

# 18:35 - 18:36（AC）
