from task_scheduler import Solution

# Create an instance of the Solution class
solution = Solution()


tasks = [
    [1, 0, 2, 3],
    [2, 1, 2, 2],
    [3, 2, 1, 5],
    [4, 5, 1, 2]
]
result = solution.schedule_tasks(tasks)

# Print the result
print(f"{result}")