from collections import defaultdict
from collections import deque

class Solution:
    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.seen = set()

    def graph(self, a): 
        for u, v in a:
            self.adjacencyList[u].append(v)
        print(self.adjacencyList)

    def dfs(self, a):
        startingNode = a[0][0]
        self.seen.add(startingNode)
        self.dfs_recursive(startingNode)

    def dfs_recursive(self, node):
        print(node)
        for nei_node in self.adjacencyList[node]:
            if nei_node not in self.seen:
                
                self.seen.add(nei_node)
                self.dfs_recursive(nei_node)

    def dfs_stack(self, a): 
        startingNode = a[0][0]
        self.seen.add(startingNode)
        stack = [startingNode]

        while stack:
            node = stack.pop()            
            print(node)
            for nei_node in self.adjacencyList[node]:
                if nei_node not in self.seen:
                    self.seen.add(nei_node)
                    stack.append(nei_node)

    def bfs_queue(self, a):
        startingNode = a[0][0]
        self.seen.add(startingNode)
        q = deque()
        q.append(startingNode)

        while q:
            node = q.pop()            
            print(node)
            for nei_node in self.adjacencyList[node]:
                if nei_node not in self.seen:
                    self.seen.add(nei_node)
                    q.append(nei_node)

    
        

    