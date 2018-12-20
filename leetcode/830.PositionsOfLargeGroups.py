class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if S == '':
            return []
        start = 0
        end = 0
        current = S[0]
        out = []
        for c in S[1:]:
            if c == current:
                end += 1
            else:
                if end - start + 1 >= 3:
                    out.append([start, end])
                start = end + 1
                end = start
                current = c
        if end - start + 1 >= 3:
            out.append([start, end])
        return out


if __name__ == '__main__':
    a = Solution()
    print(a.largeGroupPositions('abbxxxxzyy'))
