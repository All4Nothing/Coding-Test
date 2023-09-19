import sys
n, m = map(int,input().split())
dic_num = dic_name = {}
for i in range(1,n+1):
    inp = sys.stdin.readline().rstrip()
    dic_num[i] = inp
    dic_name[inp] = i
for _ in range(m):
    inp = sys.stdin.readline().rstrip()
    if inp.isdigit():
        print(dic_num[int(inp)])
    else:
        print(dic_name[inp])