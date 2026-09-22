class Solution {
    public int addDigits(int num) {
        if (num < 10) {
            return num;
        }

        int sum = 0;

        while (num/10 > 0) {
            sum = sum + (num % 10);
            num = num / 10;
        }

        sum = sum + num;

        if (sum < 10) {
            return sum;
        }

        return addDigits(sum);
    }
}