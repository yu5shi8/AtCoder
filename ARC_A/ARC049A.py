# -*- coding: utf-8 -*-
# A - "強調"
# https://atcoder.jp/contests/arc049/tasks/arc049_a

S = input()
A, B, C, D = map(int, input().split())

print(str(S[:A]) + '\"' + str(S[A:B]) + '\"' + str(S[B:C]) + '\"' + str(S[C:D]) + '\"' + str(S[D:]))

# 17:46 - 18:11（AC）
