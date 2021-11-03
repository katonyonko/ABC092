import io
import sys

_INPUT = """\
6
3
7 1
2
5
10
2
8 20
1
10
5
30 44
26
18
81
18
6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  D,X=map(int,input().split())
  A=[int(input()) for _ in range(N)]
  ans=X
  for i in range(N):
    ans+=1+(D-1)//A[i]
  print(ans)