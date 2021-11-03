import io
import sys

_INPUT = """\
6
3
3 5 -1
5
1 1 1 2 0
6
-679 -2409 -3258 3095 -3291 -4462
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  X=[0]+A+[0]
  cost=[abs(X[i+1]-X[i]) for i in range(N+1)]
  total=sum(cost)
  cost2=[abs(X[i+2]-X[i]) for i in range(N)]
  # print(cost2)
  for i in range(N):
    print(total-cost[i]-cost[i+1]+cost2[i])