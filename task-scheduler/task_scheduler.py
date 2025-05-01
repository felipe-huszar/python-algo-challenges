"""
This solution has time complexity of O(n2) because there is a linear scan for each task O(n), and 
looking up for candidates in the waiting list has a pop which is also O(n)

Space complexity is o(n) for the results list
"""

class Solution:
    def schedule_tasks(self, tasks): 
        result = []
        time = 0
        waiting = []
        i = 0

        while i < len(tasks) or waiting:            
            while i < len(tasks) and tasks[i][1] <= time:
                waiting.append(tasks[i])
                i += 1
            
            print(f'waiting: {waiting}')
            
            if waiting:
                task_to_execute = 0
                for j in range(1, len(waiting)):
                    if waiting[j][2] < waiting[task_to_execute][2]:
                        task_to_execute = j
                    elif waiting[j][2] == waiting[task_to_execute][2]:
                        if waiting[j][1] < waiting[task_to_execute][1]:
                            task_to_execute = j
                
                result.append(waiting[task_to_execute][0])
                time += waiting[task_to_execute][3]
                print(f'task {waiting[task_to_execute]} executed')
                print(f'result: {result}')
                time += 1
                waiting.pop(task_to_execute)
                
            else:
                time = tasks[i][1]

        
        return result