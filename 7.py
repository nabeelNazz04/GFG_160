'''
The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.


Examples:

Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655. Maximum Profit = 210 + 655 = 865.
'''

from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here

        result=0
        i=0
        lmin=prices[0]
        lmax=prices[0]
        n=len(prices)
        while i<n-1:
            while i<n-1 and prices[i]>=prices[i+1]:
                i+=1
            lmin=prices[i]
            ###A local minimum is the point where the stock price starts increasing after a period of decrease or remains flat.
            while i<n-1 and prices[i]<=prices[i+1]:
                i+=1
            lmax=prices[i]
            
            result+=(lmax-lmin)
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
   s=Solution()
   prices= [100, 180, 260, 310, 40, 535, 695]
   print(s.maximumProfit(prices))