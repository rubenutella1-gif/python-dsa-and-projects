class Solution:
    def lengthOfLongestSubstring(self, s):
        left=0
        max_lenght=0
        char_set=set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_lenght=max(max_lenght,right-left+1)
        return max_lenght
s = input("Enter a string: ")
obj = Solution()
result = obj.lengthOfLongestSubstring(s)
print("\nLength of Longest Substring Without Repeating Characters:", result)