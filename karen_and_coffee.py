def karen_and_coffee():
    n,k,q = map(int, input().split())

    recipe = []

    for _ in range(n):
        l,r = map(int, input().split())
        recipe.append([l,r])
    
    question = []

    for _ in range(q):
        a,b = map(int, input().split())
        question.append([a,b])

    mini, maxi = l, 200000

    points = [0 for _ in range(maxi+2)]

    for i,j in recipe:
        points[i] += 1
        points[j+1] -= 1
    
    for i in range(1,len(points)-1):
        points[i+1] = points[i+1] + points[i]

    for i in range(len(points)):
        if points[i] >=k:
            points[i] = 1
        else:
            points[i] = 0
    
    for i in range(1,len(points)-1):
        points[i+1] = points[i+1] + points[i]
    
    for a,b in question:
        print(points[b] - points[a-1])
    
karen_and_coffee()
    
