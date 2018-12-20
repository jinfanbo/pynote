class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rlist = []
        if numRows == 0:
            return rlist

        if numRows == 1:
            rlist.append([1])
            return rlist

        rlist.append([1])
        rlist.append([1, 1])
        tmp = [1, 1]
        for i in range(2, numRows):
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(tmp[j - 1] + tmp[j])

            temp.append(1)
            tmp = temp
            rlist.append(temp)

        return rlist

if __name__ == '__main__':
    a = Solution()
    print(a.generate(5))