"""
Search & Navigation Module
- BFS for unweighted graph
- UCS for weighted graph  
- A* for weighted graph with heuristic
"""
UnWeightedGraph = { 
    "Police HQ":["River Bridge","Traffic Control Center"],
    "River Bridge":["North Station","Stadium","Police HQ"],
    "North Station":["River Bridge","Traffic Control Center","Central Junction"],
    "Traffic Control Center":["Police HQ","North Station"],
    "Stadium":["River Bridge","East Market","Airport Road"],
    "East Market":["Central Junction","Stadium","City Hospital"],
    "Fire Station":["West Terminal"],
    "Central Junction":["North Station","East Market","West Terminal","South Residential"],
    "West Terminal":["Central Junction","Fire Station","Industrial Zone"],
    "Airport Road":["Stadium","South Residential"],
    "City Hospital":["East Market","South Residential"],
    "South Residential":["Airport Road","Central Junction","City Hospital"],
    "Industrial Zone":["West Terminal"]
}
WeightedGraph = { 
    "Police HQ":[("River Bridge",2),("Traffic Control Center",2)],
    "River Bridge":[("North Station",4),("Police HQ",2)],
    "North Station":[("River Bridge",4),("Traffic Control Center",2),("Central Junction",3)],
    "Traffic Control Center":[("Police HQ",2),("North Station",2)],
    "Stadium":[("Airport Road",5),("South Residential",2)],
    "East Market":[("Central Junction",3),("Stadium",2),("City Hospital",3)],
    "Fire Station":[("West Terminal",2)],
    "Central Junction":[("North Station",3),("East Market",3),("West Terminal",4),("South Residential",4)],
    "West Terminal":[("Central Junction",4),("Fire Station",2),("Industrial Zone",4)],
    "Airport Road":[("Stadium",5),("South Residential",2)],
    "City Hospital":[("East Market",3),("South Residential",3)],
    "South Residential":[("Airport Road",2),("Central Junction",4),("City Hospital",3)],
    "Industrial Zone":[("West Terminal",4)]
}
from collections import deque 
def bfs_traversal(graph, start, goal):
    if start==goal:
        return [start],0
    visited=set()
    queue = deque([(start,[start])])
    visited.add(start)
    while queue:
        node, path = queue.popleft() 
        if node== goal:
            return path,len(path) - 1 
        for neighbor in graph.get(node, []):
            if neighbor not in visited: 
                visited.add(neighbor)
                queue.append((neighbor,path+[neighbor]))
    return None,0
import heapq
def uniformCostSearch(graph, start, goal):
    pq=[(0,start,[start])] 
    visited=set()
    expO=[]
    while pq:
        cost,node,path=heapq.heappop(pq) 
        if node in visited: 
            continue
        visited.add(node) 
        expO.append(node)
        if node== goal:
            return cost,path,expO        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq,(cost+weight,neighbor,path+[neighbor])) 
    return float("inf"),None,expO
def heuristic(graph, node, goal):
    if node == goal:
        return 0
    visited = set()
    queue = deque([(node, 0)])
    visited.add(node)
    while queue:
        current, depth = queue.popleft()
        for neighbor, _ in graph.get(current, []):
            if neighbor == goal:
                return depth + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    return float('inf')
def AStar(graph, start, goal):
    heuristics=heuristic(graph,start,goal)
    pq=[(0+heuristics,0,start,[start])] 
    visited=set()
    expO=[]
    while pq:
        f,cost,node,path=heapq.heappop(pq) 
        if node in visited: 
            continue
        visited.add(node) 
        expO.append(node)
        if node== goal:
            return cost,path,expO        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                newCost=cost+weight
                f=newCost+heuristic(graph,neighbor,goal)
                heapq.heappush(pq,(f,newCost,neighbor,path+[neighbor])) 
    return float("inf"),None,expO
