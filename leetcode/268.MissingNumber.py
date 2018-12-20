class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        sum_nums = sum(nums)
        a_sum = int((1 + nums_len) * nums_len / 2)
        return a_sum - sum_nums


if __name__ == '__main__':
    a = Solution()
    print(a.missingNumber([3, 0, 1]))
    print(a.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
