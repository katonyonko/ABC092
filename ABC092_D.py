import io
import sys

_INPUT = """\
6
2 3
7 8
1 1
3 14
500 500
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=map(int,input().split())
  m=min(A,B)
  #0を黒、1を白とする
  ans=[[0]*100 if i<50 else [1]*100 for i in range(100)]
  for i in range(A-1):
    j,k=i//49,i%49
    ans[k][3*j+k]=1
  for i in range(B-1):
    j,k=i//49,i%49
    ans[99-k][3*j+k]=0
  print(100,100)
  for i in range(100):
    print(''.join(['#' if ans[i][j]==0 else '.' for j in range(100)]))