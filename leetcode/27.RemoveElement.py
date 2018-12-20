class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums),nums
if __name__ == '__main__':
    a = Solution()
    print(a.removeElement([1,2,3,4,2,2,5], 2))