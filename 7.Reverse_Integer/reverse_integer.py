# -*- coding:utf-8 -*-

class Solution:
    def reverse(self, x: int) -> int:
        if not isinstance(x,int):
            return ""
        if x < 0:
            x1 = abs(x)
            x2 = str(x1)
            x3 = x2[::-1]
            x3 = -int(x3)
            if x3 < -2 ** 31:
                return 0
        else:
            x1 = str(x)
            x2 = x1[::-1]
            x3 = int(x2)
            if x3 > 2 ** 31 - 1:
                return 0
        return x3