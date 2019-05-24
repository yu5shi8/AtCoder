# -*- coding: utf-8 -*-
# C - 755
# https://atcoder.jp/contests/abc114/tasks/abc114_c

n = int(input())

def dfs(s):
    if int(s) > n:
        return 0
    ret = 1 if all(s.count(c)>0 for c in '753') else 0
    for c in '753':
        ret += dfs(s + c)
    return ret

print(dfs('0'))

# 16:25 - 17:57
#（解説を閲覧）- 18:47
#（再挑戦）18:47 - 18:55
