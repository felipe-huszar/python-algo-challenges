# Robotic Vacuum Cleaner

## Problem Description

You are programming a robotic vacuum cleaner to navigate a room represented by a two-dimensional grid. The grid consists of empty cells and obstacles. The robot cannot move through obstacles or outside the grid boundaries.

The robot receives a sequence of movement instructions represented by the following characters:
- `U`: Move up (one cell upwards)
- `D`: Move down (one cell downwards)
- `L`: Move left (one cell to the left)
- `R`: Move right (one cell to the right)

### Rules
- If an instruction would move the robot outside the grid boundaries, the robot ignores that instruction and remains in its current position.
- If an instruction would move the robot into a cell containing an obstacle, the robot ignores that instruction and remains in its current position.

### Input

- `grid`: A two-dimensional array (`N x M`) of integers, where:
  - `0` represents an empty cell
  - `1` represents a cell containing an obstacle

- `pos`: An array of two integers `[row, column]` representing the robot's initial position. It is guaranteed that this initial position is an empty cell.

- `instructions`: A string consisting only of the characters `U`, `D`, `L`, and `R`, representing the robot's movement instructions.

### Output

Return an array of two integers `[row, column]` representing the robot's final position after processing all instructions.

### Example

#### Input
```python
grid = [
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 1, 0]
]
pos = [0, 0]
instructions = "DRDR"
```

#### Output
```python
[2, 1]
```

#### Explanation
- Move `D`: [0,0] → [1,0] (valid)
- Move `R`: [1,0] → [1,1] (obstacle → ignore)
- Move `D`: [1,0] → [2,0] (valid)
- Move `R`: [2,0] → [2,1] (valid)
