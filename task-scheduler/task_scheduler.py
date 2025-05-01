class Solution:
    def schedule_tasks(self, tasks):
        result = []
        tasks = [list(t) for t in tasks]
        waiting = []
        time = 0
        index = 0

        while index < len(tasks) or waiting:
            while index < len(tasks) and tasks[index][1] <= time:
                waiting.append(tasks[index])
                index += 1

            if waiting:
                best_idx = 0
                for i in range(1, len(waiting)):
                    if waiting[i][2] < waiting[best_idx][2]:
                        best_idx = i
                    elif waiting[i][2] == waiting[best_idx][2]:
                        if waiting[i][1] < waiting[best_idx][1]:
                            best_idx = i

                task = waiting.pop(best_idx)
                task_id, arrival, priority, duration = task

                result.append(task_id)
                time += duration
                time += 1
            else:
                time = tasks[index][1]

        return result
