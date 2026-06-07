class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                pft = prices[r] - prices[l]
                mp = max(mp, pft)
            else: 
                l=r
            r+=1

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
       