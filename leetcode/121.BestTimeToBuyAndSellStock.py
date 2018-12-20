class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sort_prices = sorted(prices, reverse=True)
        if sort_prices == prices or len(prices) == 0:
            return 0
        else:
            temp = 10000
            maxprice = 0
            for price in prices:
                if price > temp:
                    if price - temp > maxprice:
                        maxprice = price - temp
                elif price < temp:
                    temp = price
            return maxprice

if __name__ == '__main__':
    a = Solution()
    price_1 = a.maxProfit([7,6,2,4])
    price_2 = a.maxProfit([7,6,5,4])
    print(price_1)
    print(price_2)
