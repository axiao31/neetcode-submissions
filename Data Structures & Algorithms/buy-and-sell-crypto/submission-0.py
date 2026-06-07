class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        mins = prices[0]
        for i in range(len(prices)):
            mins = min(mins, prices[i])
            profit = prices[i] - mins
            mp = max(mp, profit)


        return mp

























        # max_profit = 0
        # mins = prices[0]

        # for i  in range(len(prices)):
        #     #update the mins
        #     if prices[i] < mins:
        #         mins = prices[i]

        #     #calc max_profit
        #     current_profit = prices[i] - mins

        #     #find the max_profit
        #     if current_profit > max_profit:
        #         max_profit = current_profit
        # return max_profit

        # #profit 4 5 6 0
        # #min 1
       