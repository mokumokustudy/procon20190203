#import time
#from memory_profiler import profile

N = input().split()
K = int(N[1])
N = int(N[0])
h = list(map(int, input().split()))

suml = []
suml.append(0)
suml.append(abs(h[1]-h[0]))

for e in range(2, N):
    sumpl = []
    for i in range(K):
        #print(e-(i+1))
        sumpl.append(abs(h[e]-h[e-(i+1)]) + suml[e-(i+1)])
    #print(sumpl)
    if K == 1:
        suml.append(sumpl[0])
    else:
        suml.append(min(sumpl))

print(suml[N-1])
