class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        nums_lst = [x for y in nums for x in y]
        nums_lst_len = len(nums_lst)
        if r * c != row * col:
            return nums
        else:
            new_nums_lst = list()
            for i in range(0, nums_lst_len, c):
                new_nums_lst.append(nums_lst[i:i + c])
        return new_nums_lst


if __name__ == '__main__':
    a = Solution()
    print(a.matrixReshape([[1, 2], [3, 4]], 2, 4))

# 100%
