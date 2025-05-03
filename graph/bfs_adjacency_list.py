from collections import defaultdict

class Solution:

    def __init__(self):
        self.adjacencyList = defaultdict(list)
        self.seen = set()

    def graph(self, a):
        self.adjacencyList = defaultdict(list)

        for u, v in a:
            self.adjacencyList[u].append(v)

        print(self.adjacencyList)

    def dfs(self, array):
        startingNode = array[0][0]
        self.seen = set()
        self.seen.add(startingNode)
        result = []
        self.dfs_recursive(startingNode, result)
        

    def dfs_recursive(self, node, result):
        print(node)
        result.append(node)
        for nei_node in self.adjacencyList[node]:
            if nei_node not in self.seen:
                self.seen.add(nei_node)
                self.dfs_recursive(nei_node, result)



