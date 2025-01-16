###Stock Buy and Sell (With One Limit)
'''
Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.
'''
class Solution:
    
  def maxProfit(self,prices):
    result=0
    minSoFar=prices[0]
    for i in range(1,len(prices)):
      minSoFar=min(minSoFar,prices[i])
      result=max(result,prices[i]-minSoFar)
    return result

if __name__ == "__main__":
   s=Solution()
   prices = [7, 10, 1, 3, 6, 9, 2]
   print(s.maxProfit(prices))
