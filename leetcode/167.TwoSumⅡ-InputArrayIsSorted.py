class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1, p2 = 0, len(numbers) - 1
        while True:
            sum = numbers[p1] + numbers[p2]
            if sum == target:
                return [p1 + 1, p2 + 1]
            elif sum > target:
                p2 -= 1
                if p1 == p2:
                    return None
            elif sum < target:
                p1 += 1
                if p1 == p2:
                    return None


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([2, 8, 11, 15], 9))
    print(a.twoSum([1, 5, 6, 11, 14], 25))
