# -*- coding:utf-8 -*-

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        int_str = '0123456789'
        if not str:
            return 0
        
        if str == "+" or str == "-":
            return 0

        if  str.startswith("+") or str.startswith("-"):
            if str[1] not in int_str:
                return 0
        elif str[0] not in int_str:
            return 0

        if str.startswith("+") or str.startswith("-"):
            for i in range(1,len(str)):
                if str[i] in int_str:
                    continue
                else:
                    i = i - 1
                    break
        else:
            for i in range(0, len(str)):
                if str[i] in int_str:
                    continue
                else:
                    i = i -1
                    break

        if i == len(str) - 1:
            str2int = int(str)
        else:
            str2int = int(str[:i+1:])
            
        if str2int < -2147483648:
            return -2147483648
        if str2int > 2147483647:
            return 2147483647
        return str2int

str = '+214+'
s = Solution()
print(s.myAtoi(str))