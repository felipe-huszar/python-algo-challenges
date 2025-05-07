
# Maximum Bomb Reaction Chain

You are given a list of bombs, where each bomb is represented as a triple **[x, y, R]**:

- **(x, y)**: The coordinates of the bomb on a 2D grid.
- **R**: The explosion range of the bomb, measured using the Manhattan distance.

### A reaction chain is defined as follows:

1. **Initial Detonation**: You choose one bomb to detonate manually. This bomb is the starting point of the chain.
2. **Chain Propagation**: When a bomb explodes, it simultaneously triggers every bomb that has not yet exploded and that lies within its explosion range.  
   Formally, a bomb at **(x1, y1)** detonates a bomb at **(x2, y2)** if:

   ```
   |x1 - x2| + |y1 - y2| <= R
   ```

3. **One-Time Explosion**: Each bomb can detonate only once. Bombs triggered by the chain behave in the same manner, potentially igniting further bombs.

---

## Input

- A list `bombs` of length **N**, where each element is a triple `[x, y, R]`.
- **Constraints**:
  - 1 <= N <= 1000
  - 0 <= x, y < 1000
  - 0 <= R < 100

## Output

An integer representing the maximum number of bombs that can explode in a reaction chain.

---

## Examples

### Example 1

**Input:**

```python
bombs = [[0,0,3], [2,1,2], [4,1,3], [9,3,2]]
```

**Output:**

```
3
```

**Explanation:**

1. Detonating the bomb at (0,0) triggers (2,1) — Manhattan distance = 3
2. The bomb at (2,1) then triggers (4,1) — Manhattan distance = 2
3. The bomb at (4,1) does not trigger any further bombs
4. Total: 3 bombs exploded

---

### Example 2

**Input:**

```python
bombs = [[7,5,5], [3,3,1], [10,10,3]]
```

**Output:**

```
1
```

**Explanation:**

No bomb is close enough to trigger another. Only the initial bomb explodes.
