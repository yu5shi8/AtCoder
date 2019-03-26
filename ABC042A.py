# -*- coding: utf-8 -*-
# A - 和風いろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_a

a, b, c = map(int, input().split())

if a + b + c == 17:
    print('YES')
else:
    print('NO')

'''
【参考回答】
https://atcoder.jp/contests/abc042/submissions/4715032
A = list(map(int,input().split()))
if A.count(5) == 2 and A.count(7)==1:
    print("YES")
else:
    print("NO")
'''

'''
【清書】
abc = list(map(int, input().split()))
if abc.count(5) == 2 and abc.count(7) == 1:
    print('YES')
else:
    print('NO')
'''
