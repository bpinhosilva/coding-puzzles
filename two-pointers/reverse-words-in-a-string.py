from typing import List

"""
Description: https://leetcode.com/problems/reverse-words-in-a-string/
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        str = s[::-1]
    
        start = 0
        end = 0
        
        sentence = ""
        
        while str[end] == ' ':
            end += 1
            start += 1
        
        while end < len(str):
            if str[end] == ' ':
                sentence += "".join(reversed(str[start:end]))
                
                while end < len(str) and str[end] == ' ':
                    end += 1
                
                if end < len(str):
                    sentence += ' '
                
                start = end
            
        
            end += 1
        
        sentence += "".join(reversed(str[start:end]))
        
        return sentence


    
