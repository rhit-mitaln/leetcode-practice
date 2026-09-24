class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++){
            if ((nums[i] < 10) && (nums[i] == i)){
                return nums[i];
            } else if (nums[i] >= 10) {
                int sum = 0;
                int currdig = nums[i];
                while (currdig > 0) {
                    int dig = currdig%10;
                    sum += dig;
                    currdig = currdig / 10;
                }
                if (sum == i) {
                    return sum;
                }
            }
        }
        return -1;
    }
}