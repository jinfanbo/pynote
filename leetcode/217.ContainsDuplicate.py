class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    a = Solution()
    print(a.containsDuplicate([1, 2, 3, 1]))
    print(a.containsDuplicate([1, 2, 3, 4]))
