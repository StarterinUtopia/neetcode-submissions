class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int window = s1.length();
        int boundary = s2.length();
        HashMap<Character,Integer> com = new HashMap<>();
        HashMap<Character,Integer> set = new HashMap<>();
        if (window > boundary){
            return false;
        }
        int left = 0;
        for (int i =0;i < window;i++){
            if(!com.containsKey(s1.charAt(i))){
                com.put(s1.charAt(i),1);
            }
            else
            {
                com.put(s1.charAt(i),com.get(s1.charAt(i))+1);
            }
        }
        for(int right = 0; right < boundary;right++){
            Character r = s2.charAt(right);
            Character l = s2.charAt(left);
            //add right into set
            if(!set.containsKey(r)){
                set.put(r,1);
            }
            else
            {
                set.put(r,set.get(r)+1);
            }
            // keep window valid
            if ((right-left+1) > window) {
                set.put(l,set.get(l)-1);
                left++;
            }
            if (checkPremu(com,set)){
                return true;
            }
        }
        return false;
    }
    public boolean checkPremu(HashMap<Character,Integer> com,HashMap<Character,Integer> set){
        for (Map.Entry<Character,Integer> entry : com.entrySet()){
            Character key = entry.getKey();
            Integer value = entry.getValue();
            if (!set.containsKey(key)){
                return false;
            }
            if (set.get(key)!= value){
                return false;
            }
        }
        return true;
    }
}
