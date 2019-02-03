#import time
#from memory_profiler import profile

N,W = input().split()
N = int(N)
W = int(W)

lw = []
lv = []
for i in range(N):
    w,v = list(map(int, input().split()))
    lw.append(w)
    lv.append(v)

def calc(clw,clv,cw,cv):
    rs = []
    for i,val in enumerate(clw):
        if cw-val<=0:
            continue
        rs.append(calc(clw[:i]+clw[i+1:],clv[:i]+clv[i+1:],cw-val,cv+clv[i]))
    if len(rs) == 0:
        return cv
    else:
        return max(rs)

rs = []
for i,val in enumerate(lw):
    if W-val<=0:
        continue
    rs.append(calc(lw[:i]+lw[i+1:],lv[:i]+lv[i+1:],W-val,lv[i]))

print(max(rs))
