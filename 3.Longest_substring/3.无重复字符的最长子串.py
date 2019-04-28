#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            d= {}
            for i in range(len(s)):
                tmp = [] 
                tmp.append(s[i])
                for j in range(i+1,len(s)):
                    if s[j] not in tmp:
                        tmp.append(s[j])
                    else:
                        break
                d[i] = len(tmp)
            d = sorted(d.items(),key=lambda item:item[1],reverse=True)
            longest = d[0][1]
            return longest
        else:
            return 0

s = "abcabcbb"
l = Solution()
print(l.lengthOfLongestSubstring(s))

   