class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int th = threshold*k;
        int sum = 0;
        int count = 0;
        for(int right = 0 ; right < arr.length; right++){
            sum+=arr[right];
            if (right >= k-1){
                if (sum >= th){
                    count++;
                } 
                sum -= arr[right -k + 1];
            }
        }
        return count;
    }
}