class Solution1:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))


class Solution2:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        a1 = []
        b = len(A[0])
        for i in range(b):
            a = [x[i] for x in A]
            a1.append(a)
        return a1


if __name__ == '__main__':
    a = Solution1()
    print(a.transpose([[1, 2, 3, 3], [4, 5, 6, 3], [7, 8, 9, 3]]))
    a = Solution2()
    print(a.transpose([[1, 2, 3, 3], [4, 5, 6, 3], [7, 8, 9, 3]]))
