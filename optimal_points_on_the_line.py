def optima_point_on_line():
    n = int(input())
    points = list(map(int, input().split()))
    distances = {}
    points.sort()
    print(points[(n - 1) // 2])
    return
optima_point_on_line()
