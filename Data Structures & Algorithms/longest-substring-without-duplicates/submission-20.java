class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2){
            return s.length();
        }
        HashMap<Character,Integer> mp = new HashMap<>();
        int l = 0;
        int r = 0;
        int res = 0;
        while (r < s.length()){
            if (mp.containsKey(s.charAt(r))){
                l = Math.max(mp.get(s.charAt(r))+1,l);                
            }
            mp.put(s.charAt(r),r);
            res = Math.max(r-l+1 , res);
            r++;
        }
        return res;
    }
}

