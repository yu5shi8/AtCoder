# -*- coding: utf-8 -*-
# A - 饅頭
# https://atcoder.jp/contests/abc037/tasks/abc037_a

a, b, c = map(int, input().split())

ans_a = c // a
ans_b = c // b

print(max(ans_a, ans_b))

# 20:49 - 20:52
