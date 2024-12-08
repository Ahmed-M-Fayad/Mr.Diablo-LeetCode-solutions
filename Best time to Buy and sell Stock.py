
                              # Best time to Buy and sell Stock
                              #            Big O(n)
"""
I will explain This Solution:
           - note That You Should Buy in Day Before The Day You Want To sail in it
           - so I will choose The Minium Stock precede  The Day I Want To sail in it
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #    the frist Value for max profit
        max_profit = 0
        #    the frist Value for  Minium price
        min_val = prices[0]
        for val in  prices:
            # compare  and choose maxmum  between max profit and the diffrence of the present price and  Minium price
            max_profit = max(max_profit , val - min_val  )
            # compare  and choose Minium  between Minium price and the  present price
            min_val = min( min_val , val)


        return max_profit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))