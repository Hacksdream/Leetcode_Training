# -*- coding:utf-8 -*-

import re

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        match_mode = re.compile('^([+-]?\d+).*')
        match_int = re.match(match_mode, str)
        if not match_int:
            return 0
        result = int(match_int.group(1))

        if result < -2147483648:
            return - 2147483648
        elif result > 2147483647:
            return 2147483647 
        return result

str = '+214 22+'
s = Solution()
print(s.myAtoi(str))
