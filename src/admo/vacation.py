#import time
#from memory_profiler import profile

N = int(input())
al = []
for i in range(N):
    h = list(map(int, input().split()))
    al.append(h)

s = 0
def calc(rs,si,srs):
    l = rs[0]
    srs += l[si]
    if (len(rs)==1):
        return srs
    else:
        if si == 0:
            return max(calc(rs[1:],1,srs), calc(rs[1:],2,srs))
        elif si == 1:
            return max(calc(rs[1:],0,srs), calc(rs[1:],2,srs))
        elif si == 2:
            return max(calc(rs[1:],0,srs), calc(rs[1:],1,srs))

print(max(calc(al,0,0),calc(al,1,0),calc(al,2,0)))
