"""
This solution has
time complexity = O(n2)
space complexity = O(n)
"""

class Solution:
    def circleGame(self, n):
        players = list(range(1, n+1))
        j = 0
        
        for k in range(1, n):
            print(players)
            j = (j + k) % len(players)
            players.pop(j)
            j = j % len(players)

        return players[0]