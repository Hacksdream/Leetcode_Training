# -*- coding:utf-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        s_reverse = s[::-1]
        d = {}
        if len(set(s)) == 1:
            return s
        for index in range(len(s)):                
            for length in range(index,len(s)):
                if index == length:
                    substring = s[index]
                else:
                    substring = s[index:length+1]
                    if substring != substring[::-1]:
                        continue
                if substring in s_reverse:
                    d[substring] = len(substring)
        d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        longest_palidrome = d[0][0]
        return longest_palidrome