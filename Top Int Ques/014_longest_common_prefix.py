class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 0:
            return result
        if len(strs) == 1:
            return strs[0]
        
        all_lengths = []
        for word in strs:
            all_lengths.append(len(word))
        min_length = min(all_lengths)
        if min_length == 0:
            return result
        
        num_words = len(strs)
        common_letters = []
        
        count = 0
        while count < min_length:
            
            for word in strs:
                temp = word[count]
                common_letters.append(temp)
            count += 1
            
            if (all(x == common_letters[0] for x in common_letters) == True): 
                result = result + common_letters[0]
                common_letters = []
            else:
                return result
            
        return result
