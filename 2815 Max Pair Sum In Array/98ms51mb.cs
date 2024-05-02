public class Solution {
    public int MaxSum(int[] nums) {
        int ans = -1;
        Dictionary<int, int> map = new();
        for(int i = 0; i < nums.Length; i++){
            int maxDigit = getMaxDigit(nums[i]);
            if(map.ContainsKey(maxDigit)){
                ans = Math.Max(ans, map[maxDigit] + nums[i]);
                map[maxDigit] = Math.Max(map[maxDigit], nums[i]);
            }else{
                map.TryAdd(maxDigit, 0);
                map[maxDigit] = nums[i];
            }
        }

        return ans;
    }

    private int getMaxDigit(int num){
        int maxDigit = 0;
        while(num != 0){
            maxDigit = Math.Max(maxDigit, num%10);
            num /= 10; 
        }
        return maxDigit;
    }
}
