class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals is None:
            return []
        
        # Sort the pairs in intervals by the first value
        intervals = sorted(intervals, key=lambda x:x[0])
        
        results = []
        
        for pair in intervals:
            if not results or results[-1][1] < pair[0]:
                results.append(pair)
            else:
                results[-1][1] = max(results[-1][1], pair[1])
        
        return results
