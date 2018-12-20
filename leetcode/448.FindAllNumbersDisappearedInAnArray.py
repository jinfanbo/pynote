class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        new_nums = set(range(1, nums_len + 1))
        nums = set(nums)
        return list(new_nums.difference(nums))


if __name__ == '__main__':
    a = Solution()
    new_nums = a.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(new_nums)
