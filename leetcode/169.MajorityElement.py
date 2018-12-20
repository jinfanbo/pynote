class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = set(nums)
        max_num = 0
        max_element = 0
        for i in new_nums:
            count = nums.count(i)
            if max_num < count:
                max_num = count
                max_element = i
        return max_element


if __name__ == '__main__':
    a = Solution()
    print(a.majorityElement([3, 2, 3]))
    print(a.majorityElement([2, 2, 1, 1, 1, 2, 2]))
