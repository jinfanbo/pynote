class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        flag = 0
        for num in nums:
            if num != 0:
                nums[flag] = num
                flag += 1
        for i in range(flag, nums_len):
            nums[i] = 0


if __name__ == '__main__':
    a = Solution()
    nums = [0, 1, 0, 3, 12]
    a.moveZeroes(nums)
    print(nums)
