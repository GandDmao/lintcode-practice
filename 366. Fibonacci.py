class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        a = 0
        b = 1
        for i in range(n-1):
            a, b = b, a+b
        return a





if __name__ == "__main__":
    so = Solution()
    print(so.fibonacci(40))