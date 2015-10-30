"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        # write your code here
        if len(intervals) == 0:
            results.append(newInterval)
        for i in range(len(intervals)):
            if intervals[i].end < newInterval.start:
                results.append(intervals[i])
            elif intervals[i]. start > newInterval.end:
                if newInterval not in results:
                    results.append(newInterval)
                results.append(intervals[i])
            else:
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.end = max(intervals[i].end, newInterval.end)
        if len(results) == 0 or newInterval.start > results[-1].end:
            results.append(newInterval)
        return results
