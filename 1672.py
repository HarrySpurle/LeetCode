class Solution:
    def maximumWealth(self, accounts):
        greatest_wealth = 0
        for person in accounts:
            networth = 0
            for location in person:
                networth += location
            if networth > greatest_wealth:
                greatest_wealth = networth
        return greatest_wealth