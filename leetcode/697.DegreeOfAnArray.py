class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, counter, res, degree = {}, {}, 0, 0
        for i, v in enumerate(nums):
            # 各元素第一次出现的位置
            first.setdefault(v, i)

            # 求nums最大度数
            counter[v] = counter.get(v, 0) + 1
            if counter[v] > degree:
                degree = counter[v]
                #     |--|
                # 1， 2， 2， 3， 4， 1， 2
                #     |-----------------|
                # 1， 2， 2， 3， 4， 1， 2
                res = i - first[v] + 1
            elif counter[v] == degree:
                # 比较选最短
                #     |--|
                # 1， 2， 2， 3， 4， 1， 2
                # |-----------------|
                # 1， 2， 2， 3， 4， 1， 2
                res = min(res, i - first[v] + 1)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
