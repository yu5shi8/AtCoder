# -*- coding: utf-8 -*-
# A - スーパーICT高校生
# https://atcoder.jp/contests/arc022/tasks/arc022_1

S = input()
ans = ''

for s in S:
    if len(ans) == 0 and (s == 'I' or s == 'i'):
        ans += s
    elif len(ans) == 1 and (s == 'C' or s == 'c'):
        ans += s
    elif len(ans) == 2 and (s == 'T' or s == 't'):
        ans += s

if len(ans) == 3:
    print('YES')
else:
    print('NO')

# 10:41 - 10:47（AC）
