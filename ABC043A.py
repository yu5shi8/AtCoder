# -*- coding: utf-8 -*-
# A - キャンディーとN人の子供イージー
# https://atcoder.jp/contests/abc043/tasks/abc043_a

n = int(input())
children = list(i for i in range(1, n+1))
answer = sum(children)
print(answer)
