class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= (-2)**31 or x >= 2**31 - 1:
            return 0
        else:
            numinstr = str(x)
            if x >= 0:
                revstr = numinstr[::-1]
            else:
                temp = numinstr[1:]
                temp1 = temp[::-1]
                revstr = '-' + temp1
            if int(revstr) <= (-2)**31 or int(revstr) >= 2**31 - 1:
                return 0
            else:
                return int(revstr)
