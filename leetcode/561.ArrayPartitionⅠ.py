class Solution1:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


class Solution2:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        nums_len = len(nums)
        for i in range(0, nums_len, 2):
            result += nums[i]
        return result


if __name__ == '__main__':
    a = Solution1()
    print(a.arrayPairSum([1, 4, 3, 2]))
    a = Solution2()
    print(a.arrayPairSum([1, 4, 3, 2]))
