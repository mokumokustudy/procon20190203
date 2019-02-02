n = int(input())
inputs = input().split(" ")
l = [int(s) for s in inputs]

def calc(rl, ns, skip):
    v = rl[len(rl)-1]
    # print(rl,v,ns)
    lrl = len(rl)
    
    if lrl == 1:
        return ns
    if lrl == 2:
        v1 = rl[len(rl)-2]
        return ns+abs(v-v1)
    if lrl == 3:
        v1 = rl[len(rl)-2]
        v2 = rl[len(rl)-3]
        ns1 = ns + abs(v-v2)
        ns2 = ns + abs(v-v1) + abs(v1-v2)
        return min(ns1,ns2)
    else:
        v1 = rl[len(rl)-2]
        v2 = rl[len(rl)-3]
        return min(calc(rl[:len(rl)-1],ns+abs(v-v1),True),calc(rl[:len(rl)-2],ns+abs(v-v2),False))

print(calc(l,0,False))
