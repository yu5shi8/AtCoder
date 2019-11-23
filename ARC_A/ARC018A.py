# -*- coding: utf-8 -*-
# A - BMI
# https://atcoder.jp/contests/arc018/tasks/arc018_1

Height, BMI = map(float, input().split())
Height /= 100

Weight = (Height**2) * BMI

print(Weight)

# 20:07 - 20:09（AC）
