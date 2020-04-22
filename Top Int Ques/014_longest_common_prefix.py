class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        all_lengths = [len(s) for s in strs]
        min_length = min(all_lengths)
        
        if min_length == 0:
            return ""

        result = ""

        for i in range(min_length):
            all_letters = [s[i] for s in strs]

            if len(set(all_letters)) == 1:
                result = result + all_letters[0]
            else:
                return result
        return result
