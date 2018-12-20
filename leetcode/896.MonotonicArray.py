class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        a = sorted(A)
        b = a[::-1]
        return A == a or A == b


if __name__ == '__main__':
    a = Solution()
    print(a.isMonotonic([1, 2, 2, 1]))
