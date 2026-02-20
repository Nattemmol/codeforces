def polycarp_training():
    n = int(input())
    problems = list(map(int, input().split()))

    problems.sort()
    days = 0
    k = 1
    for i in range(len(problems)):
        if problems[i] >= k:
            days += 1
            k += 1
    print(days)
    return
polycarp_training()
