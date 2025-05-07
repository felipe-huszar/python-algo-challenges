from collections import defaultdict

class Solution:
    def max_explosion_radius(self, bombs):
        # build adjacency list

        graph = defaultdict(list)

        # create adjacency list
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]

                if abs(x1-x2) + abs(y1-y2) <= r1:
                    graph[i].append(j)

        

        # dfs 
        def dfs(node, seen):
            seen.add(node)
            for nei_node in graph[node]:
                if nei_node not in seen:
                    dfs(nei_node, seen)                    
        
        max_bombs = 0
        
        # detonate each bomb
        for i in range(len(bombs)):
            seen = set()
            dfs(i, seen)
            max_bombs = max(len(seen), max_bombs)

        return max_bombs

