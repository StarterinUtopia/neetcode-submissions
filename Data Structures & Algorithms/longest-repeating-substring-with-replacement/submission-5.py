class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        max_freq = 0
        max_count = 0
        left = 0  
        for right in range(len(s)):
        # 1. 将右指针字符加入字典频次
            char[s[right]] = char.get(s[right],0)+1
        # 2. 动态更新当前窗口内出现最多的字符频次
            max_freq = max(max_freq,char[s[right]]) 
        # 3. 如果需要替换的字符数量 (窗口长度 - 最高频次) >        k，则收缩左边界
            while(right-left+1 - max_freq) > k:
                char[s[left]] -= 1
                left += 1
        # 4. 更新最大符合条件的窗口长度
            max_count = max(max_count, right - left + 1 )
        return max_count
            

                


                
             


        return max_count
            


              



        