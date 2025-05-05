from dfs_bfs_adjacency_list import Solution

a = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

solution = Solution()
solution.graph(a) 
solution.bfs_queue(a)

