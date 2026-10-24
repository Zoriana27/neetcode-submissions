class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #if newInterval ends before the curr one starts
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:#if the newInterval starts after the curr one ends
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

        