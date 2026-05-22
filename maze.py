import matplotlib.pyplot as plt
import numpy as np
from collections import deque

maze = np.array([
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
])

start = (0, 0)
goal = (4, 4)

rows, cols = maze.shape

def draw(grid, visited=set(), path=[]):
    display = np.copy(grid)
 
    for (x, y) in visited:
        display[x][y] = 0.5
 
    for (x, y) in path:
        display[x][y] = 2
 
    plt.clf()
    plt.imshow(display)
    plt.xticks([])
    plt.yticks([])
    plt.pause(0.1) 

def bfs():
    visited = set()
    parent = {}
    queue = deque([start])
 
    visited.add(start)
 
    while queue:
        x, y = queue.popleft()
 
        draw(maze, visited)
 
        if (x, y) == goal:
            break
 
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
 
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
 
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent.get(node)
        if node is None:
            return []
            
    path.append(start)
    path.reverse()
    return path

plt.figure()
path = bfs()
draw(maze, path=path)
plt.show()
