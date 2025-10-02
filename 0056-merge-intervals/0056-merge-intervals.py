class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            a, b = merged_intervals[-1]
            c, d = intervals[i]
            if c<=b:
                current_interval = [min(a, c), max(b, d)]
                merged_intervals[-1] = current_interval
            else:
                merged_intervals.append([c, d])
        return merged_intervals