""" Use DP as a way to solve recusively over iteration of coins"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #first check special cases
        if amount <=0:
            return None
        combinations = [0]*(amount+1)
        #set index 0 = 1, since amount should never be 0
        combinations[0] = 1
        #iterate through each coin  in coins
        for coin in coins:
            for i in range(1, len(combinations)):
                if i >= coin:
                    combinations[i] += combinations[i - coin]