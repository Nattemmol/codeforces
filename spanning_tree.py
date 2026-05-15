from collections import defaultdict
import heapq


def spanning_tree():
    n,m = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(m):
        b,c,w = map(int,input().split())
        graph[b].append((w,c))
        graph[c].append((w,b))
    
    heap = [(0,1)]
    visited = set()
    ans = 0
    while heap:
        w,u = heapq.heappop(heap)
        if u in visited:
            continue
        ans += w
        visited.add(u)

        for wegh,negh in graph[u]:
            if negh not in visited:
                heapq.heappush(heap,(wegh,negh))
    print(ans)   

spanning_tree()

