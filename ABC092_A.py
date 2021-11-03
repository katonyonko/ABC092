import io
import sys

_INPUT = """\
6
600
300
220
420
555
555
400
200
549
817
715
603
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X=[int(input()) for _ in range(4)]
  print(min(X[0],X[1])+min(X[2],X[3]))