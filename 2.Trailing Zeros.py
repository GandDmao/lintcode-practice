#尾部的零
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count=0
        p=n
        while (p!=0):
            p=p//5
            count+=p
        return count



