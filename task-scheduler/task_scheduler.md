# Task Scheduler #

You are given an assignment to write the logic for a task scheduler on a single-core computer. For simplicity, assume that tasks cannot be preempted.
This means that once the CPU starts executing a task, it will run it to completion.
Any other task that needs to be executed while the CPU is busy will have to wait until it finishes the current task.

Each task has an identifier, an arrival time, a priority, and a duration.
The task scheduler should honor the following principles:

## Rules ##

- Immediate Start:
If a task arrives and the CPU is idle (i.e., it is not running any task), that task should start running immediately.

- Highest Priority First:
If there are multiple tasks to run, the scheduler should choose the one with the highest priority.

- Arrival Order Break Ties:
If there are multiple tasks with the same priority, the scheduler should choose the one that arrived first.

- Non-Preemption & Delay:
If a task finishes at instant T and there are other tasks waiting to be executed, the next task will start at instant T+1.

- Priority Definition:
Given two tasks 1 and 2, task 1 is said to have a higher priority than task 2 if priority1 < priority2.

- Scheduling Decision Time:
The scheduling decisions happen at the next instant after the running task finishes.
Specifically, if a task completes at time T, the scheduler chooses the next task to run at time T+1.
If any new task arrives exactly at time T+1, it competes with all other waiting tasks to run next.

## Task Duration ## 

Task duration is calculated inclusively:
A task with duration D that starts at time T will finish at time T + D - 1.

## Write a Function ##

Write a function that computes the correct order of execution of tasks from an array tasks.
Each entry in the array is an array with 4 integers:

```[task_id, arrival_time, priority, duration]```

The tasks are ordered by arrival time, and you can assume that:

- No two tasks have the same arrival time.
- Each task will have a unique task identifier.

The output should be an array of identifiers (integers) representing the order of execution of tasks.

## Input

- A list of arrays where each sub-array contains:
    - task_id (integer)
    - arrival_time (integer)
    - priority (integer, smaller is better)
    - duration (integer)

## Output

- A list of integers representing the order of task executions.

## Example 1

```
tasks = [
    [1, 0, 2, 3],
    [2, 1, 2, 2],
    [3, 2, 1, 5],
    [4, 5, 1, 2]
]
```

### Explanation:

- Task 1 arrives at time 0 and starts running immediately. Runs from time 0 to 2.
- Task 2 arrives at time 1 but has to wait.
- Task 3 arrives at time 2 but has to wait.
- At time 3, task 3 starts because it has higher priority than task 2.
- Task 3 runs from time 3 to 7.
- Task 4 arrives at time 5 and waits.
- At time 8, task 4 starts.
- Task 4 runs from time 8 to 9.
- At time 10, task 2 starts.
- Task 2 runs from time 10 to 11.

Thus, the order of execution is:

```[1, 3, 4, 2]```

## Example 2

```
tasks = [
    [1, 0, 1, 4],
    [2, 1, 3, 2],
    [3, 2, 2, 1],
    [4, 3, 1, 3]
]
```

## Important Notes

- CPU cannot preempt once it starts executing a task.
- Must wait one unit of time after a task finishes before starting a new task.
- Always prefer the task with the smallest priority number.
- If priority is tied, prefer the task that arrived first.

## Constraints

- Number of tasks: up to 1000.
- Task identifiers are unique.
- No two tasks have the same arrival time.