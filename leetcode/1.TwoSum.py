class Solution:
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
        result = list()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                result.append((nums[i], nums[hash_map[target - x]]))
                # return [i, hash_map[target - x]]
            hash_map[x] = i
        return result


if __name__ == '__main__':
    a = Solution()
    result = a.twosum([2, 7, 8, 9, 11, 1, 0], 11)
    print(result)
