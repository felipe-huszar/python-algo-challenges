"""
This solution has time complexity of O(n log n) because there is a linear scan for each task O(n), and 
using the min-heap to look for candidates has complexity of log n

Space complexity is o(n) for the results list
"""

import heapq

class Solution:
    def schedule_tasks(self, tasks): 
        result = []
        time = 0
        waiting = []
        i = 0

        while i < len(tasks) or waiting:            
            while i < len(tasks) and tasks[i][1] <= time:
                heapq.heappush(waiting, (tasks[i][2], tasks[i][1], i))
                i += 1
            
            if waiting:
                priority, arrival, task_index = heapq.heappop(waiting)
                
                result.append(tasks[task_index][0])
                time += tasks[task_index][3]
                time += 1
            else:
                time = tasks[i][1]

        
        return result