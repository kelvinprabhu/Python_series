class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # result = []
        # result.append(s[0])
        # for i in len(s):
        #     if s[i+1] in s:
        #         pass:
        #         else:
        #             result
        arr = [False]*128
        l = r = 0
        max_len = 0
        
        while r < len(s):

            if not arr[ord(s[r])]:
                arr[ord(s[r])] = True
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                arr[ord(s[l])] = False
                l += 1
        return max_len


        
            



             