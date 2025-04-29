# Circle Game

## Problem Description

There are **N players** (numbered from **1** to **N**) arranged in a **circle**.  
- Player 1 is next to Player 2, Player 2 is next to Player 3, ..., and Player N is next to Player 1, forming a continuous loop.

The game consists of **N-1 rounds**. In each round, exactly **one player is eliminated**.

The elimination process is conducted by a **judge** who moves around the circle according to the following rules:

- **Initially**, the judge stands in front of **Player 1**.
- **In round K** (where K ranges from **1 to N-1**):
  - The judge moves exactly **K steps clockwise**, skipping eliminated players.
  - The player the judge lands on is **eliminated**.
- **After eliminating a player**, the judge moves exactly **1 additional step clockwise** to stand in front of the next available player, preparing for the next round.

The process continues until only **one player** remains, who is declared the winner.

---

## Input

- A single integer **N** (1 ≤ N ≤ 1000), representing the number of players.

## Output

- A single integer representing the **number of the winning player**.

---

## Example

### Input

5

### Output

4

### Explanation
- Initial circle: [1, 2, 3, 4, 5]
- Round 1: Judge moves 1 step → eliminates Player 2 → circle becomes [1, 3, 4, 5]
- Round 2: Judge moves 2 steps → eliminates Player 5 → circle becomes [1, 3, 4]
- Round 3: Judge moves 3 steps → eliminates Player 1 → circle becomes [3, 4]
- Round 4: Judge moves 4 steps → eliminates Player 3 → **Winner: Player 4**

---
