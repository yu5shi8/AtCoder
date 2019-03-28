# -*- coding: utf-8 -*-
# A - キャンディーと2人の子供
# https://atcoder.jp/contests/abc047/tasks/abc047_a
abc = sorted(list(map(int, input().split())))

if abc[0] + abc[1] == abc[2]:
    print('Yes')
else:
    print('No')
