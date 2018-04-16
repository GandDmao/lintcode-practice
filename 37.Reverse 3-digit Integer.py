class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        a=number%10
        b=(number//10)%10
        c=number//100
        reversenum=a*100+b*10+c
        return reversenum

if __name__ == "__main__":
    so = Solution()
    print(so.reverseInteger(123))
