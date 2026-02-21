def this_is_the_last_time():
    t = int(input())
    for _ in range(t):


        n,k = map(int, input().split())
        game = [[0]*3 for _ in range(n)]


        for i in range(n):
            l,r,real = map(int, input().split())
            game[i][0] = l
            game[i][1] = r
            game[i][2]  = real


        game.sort(key = lambda  x: x[0])
        

        for a,b,c in game:
            if b>= k >= a:
                if c > k:
                   k = c
            
        print(k)
            
    return
this_is_the_last_time()
