class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int j = 0; j < nums.length; j++){
            if (map.get(nums[j]) != null){
                if (Math.abs(j-map.get(nums[j]))<=k){
                    return true;
                }
            }
            map.put(nums[j],j);
        }
        return false;
    }
}