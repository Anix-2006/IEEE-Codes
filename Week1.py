
print("Enter: n m F (stations, connections, max_fuel):")
while True:
    try:
        line = input().split()
        if len(line) >= 3:  
            n = int(line[0])
            m = int(line[1])
            F = int(line[2])
            break
        else:
            print("Please enter exactly 3 numbers separated by spaces:")
    except ValueError:
        print("Please enter valid integers:")

print(f"Now enter {m} connections in format: u v time cost:")

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, time, cost = map(int, input().split())
    graph[u].append((v, time, cost))
    graph[v].append((u, time, cost)) 


class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self,item):
        self.heap.append(item)
        self.move_up(len(self.heap) - 1) 

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.move_down(0)
        return min_item

    def empty(self):
        return len(self.heap) == 0

    def move_up(self,index):
        while index > 0:
            parent = (index-1) // 2
            if self.heap[parent] <= self.heap[index]:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def move_down(self,index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


Queue = PriorityQueue()
Queue.push((0,1,F)) 
visited = set()
result = -1
while not Queue.empty():
    current_time, station, fuel = Queue.pop()

    if station == n:
        result = current_time
        break
    state = (station, fuel)
    if state in visited:
        continue
    visited.add(state)

    for next_station, travel_time, fuel_cost in graph[station]:
        remaining_fuel = fuel - fuel_cost
        if remaining_fuel >= 0:
            new_time = current_time + travel_time
            new_state = (next_station, remaining_fuel)
            if new_state not in visited:
                Queue.push((new_time, next_station, remaining_fuel))

    print("The minimum possible travel time within the fuel budget is: ", result)  
    if result == -1:
        print("Therefore, no route is possible within the fuel budget.")



    
