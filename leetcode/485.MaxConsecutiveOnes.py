class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        flag = 0
        for i in nums:
            if i == 1:
                sum += 1
            else:
                if sum >= flag:
                    flag, sum = sum, 0
                else:
                    sum = 0
        if flag > sum:
            return flag
        else:
            return sum


if __name__ == '__main__':
    a = Solution()
    print(a.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
