class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b, c = sum(A), sum(B), set(B)
        for member in A:
            flag = (b - a) // 2 + member
            if flag in c:
                return [member, flag]


if __name__ == '__main__':
    a = Solution()
    print(a.fairCandySwap([1, 2], [2, 3]))
    print(a.fairCandySwap([1, 1], [2, 2]))
    print(a.fairCandySwap([2], [1, 3]))
    print(a.fairCandySwap([1, 2, 5], [2, 4]))
