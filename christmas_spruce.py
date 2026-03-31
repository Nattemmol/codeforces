from collections import Counter


def christmas_spruce():
    n = int(input())
    p = []
    po = []
    for i in range(1,n):
        pi = int(input())
        p.append((i+1,pi))
        po.append(pi)
    
    count = Counter(po)

    for i,j in p:
        if i in count:
            count[j] -= 1

    for k,v in count.items():
        if v < 3:
            print("No")
            return
    print("Yes")

christmas_spruce()
