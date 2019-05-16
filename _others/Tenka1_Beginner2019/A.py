# -*- coding: utf-8 -*-
# A - On the Way
# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_a

a, b, c = map(int, input().split())

if a<c<b or b<c<a:
    print('Yes')
else:
    print('No')
