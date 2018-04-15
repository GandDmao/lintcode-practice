class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        import ctypes
        a=ctypes.c_int32(a).value
        b = ctypes.c_int32(b).value
        while(b!=0):
            carry=ctypes.c_int32(a&b).value
            a=ctypes.c_int32(a^b).value
            b=ctypes.c_int32(carry<<1).value
        return a



