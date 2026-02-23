def sort_and_compare():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        b = []
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        op = []
        count = 0
        for _ in range(n):
            for i in range(n-1):
                if a[i] > a[i+1]:
                    a[i],a[i+1] = a[i+1],a[i]
                    op.append([1,i+1])
                    count += 1
        


        for _ in range(n):
            for i in range(n-1):
                if b[i] > b[i+1]:
                    b[i],b[i+1] = b[i+1],b[i]
                    op.append([2,i+1])
                    count += 1
        for i in range(n):
            if a[i] > b[i]:
                a[i],b[i] = b[i],a[i]
                op.append([3,i+1])
                count += 1


        print(count)
        if count > 0:
            for i,j in op:
                print(i,j)
    return
sort_and_compare()
