
graph = {'A': ['B', 'C'],
         'B': ['A', 'E'],
         'C': ['A'],
         'D': ['E'],
         'E': ['B','D']}


def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [start]
    if start == goal:
        return "That was easy! Start = goal"
    keys=list(graph.keys())
    
    while keys:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
        keys.pop()

    return "So sorry, but a connecting path doesn't exist :("
 
bfs_shortest_path(graph, 'A', 'D')
