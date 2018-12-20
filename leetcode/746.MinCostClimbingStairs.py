class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        step1, step2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            cur = min(step1, step2) + cost[i]
            step1, step2 = step2, cur
        return min(step1, step2)
if __name__ == '__main__':
    a = Solution()
    print(a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
    print(a.minCostClimbingStairs([1,1,100,1,1,100,1,1,100,1]))