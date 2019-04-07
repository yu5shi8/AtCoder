# -*- coding: utf-8 -*-
# A - Task Scheduling Problem
# https://atcoder.jp/contests/abc103/tasks/abc103_a

a1, a2, a3 = map(int, input().split())

task = [a1, a2, a3]
task = sorted(task)

ans = abs(task[0] - task[1]) + abs(task[1] - task[2])
print(ans)

# 最大値と最小値の差が答えになる問題
# a1, a2, a3 = map(int, input().split())
# ans = max(a1, a2, a3) - min(a1, a2, a3)
# print(ans)
