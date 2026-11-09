class Solution {
public:
    int search(vector<int>& nums, int target) {
        int right = 0;
        int left = nums.size()-1;
        while (right <= left){
            int mid = (right+left)/2;
            if (nums[mid]==target){
                return mid;
            }
            else if (nums[mid]>target){
                left = mid-1;
            }
            else {//if nums[mid]<target
                right = mid+1;
            }
        }
        return -1;
    }
};
