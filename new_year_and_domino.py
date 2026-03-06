def new_year_and_domino():
    h,w = map(int, input().split())
    grid = []

    for _ in range(h):
        s = input()
        grid.append(s)
    
    q = int(input())

    queries = []
    
    for _ in range(q):
        r1,c1,r2,c2 = map(int, input().split())

        queries.append([r1,c1,r2,c2])
    
    
    h_prefix_2d = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for i in range(h):
        for j in range(1, w):
            val = 1 if grid[i][j] == '.' and grid[i][j-1] == '.' else 0
            h_prefix_2d[i+1][j+1] = val + h_prefix_2d[i+1][j] + h_prefix_2d[i][j+1] - h_prefix_2d[i][j]

    v_prefix_2d = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for j in range(w):
        for i in range(1, h):
            val = 1 if grid[i][j] == '.' and grid[i-1][j] == '.' else 0
            v_prefix_2d[i+1][j+1] = val + v_prefix_2d[i+1][j] + v_prefix_2d[i][j+1] - v_prefix_2d[i][j]


    for r1, c1, r2, c2 in queries:
        h_sum = 0
        if c2 > c1:
            h_sum = h_prefix_2d[r2][c2] - h_prefix_2d[r1-1][c2] - h_prefix_2d[r2][c1] + h_prefix_2d[r1-1][c1]
        
        v_sum = 0
        if r2 > r1:
            v_sum = v_prefix_2d[r2][c2] - v_prefix_2d[r1][c2] - v_prefix_2d[r2][c1-1] + v_prefix_2d[r1][c1-1]
            
        print(h_sum + v_sum)


new_year_and_domino()
