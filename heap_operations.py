import heapq
import sys

def heap_operations():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    n = int(input_data[0])
    heap = []
    ans = []
    
    for i in range(1, n + 1):
        line = input_data[i].split()
        command = line[0]
        
        if command == "insert":
            val = int(line[1])
            heapq.heappush(heap, val)
            ans.append(f"insert {val}")
            
        elif command == "removeMin":
            if not heap:
                heapq.heappush(heap, 0)
                ans.append("insert 0")
            heapq.heappop(heap)
            ans.append("removeMin")
            
        elif command == "getMin":
            val = int(line[1])
            while heap and heap[0] < val:
                heapq.heappop(heap)
                ans.append("removeMin")
            
            if not heap or heap[0] > val:
                heapq.heappush(heap, val)
                ans.append(f"insert {val}")
                
            ans.append(f"getMin {val}")
            
    print(len(ans))
    for op in ans:
        print(op)

if __name__ == '__main__':
    heap_operations()
