class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3],nums[-1] * nums[-2] * nums[0],nums[-1] * nums[0] * nums[1])


if __name__ == '__main__':
    a = Solution()
    print(a.maximumProduct([-5, 1, 2, 3, 4]))
