class Solution {
    public int[] findDegrees(int[][] matrix) {
        int[] ans = new int[matrix[0].length];
        for (int i = 0; i < matrix[0].length; i++) {
            int count = 0;
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 1) {
                    count++;
                }
            }
            ans[i] = count;
        }
        return ans;
    }
}