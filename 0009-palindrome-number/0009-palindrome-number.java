class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        return isPalindromeHelper(s);
    }
    public boolean isPalindromeHelper(String s){
       if (s.length() <= 1) {
            return true; 
        }

        if (s.charAt(0) != s.charAt(s.length() - 1)) {
            return false;
        }

        return isPalindromeHelper(s.substring(1, s.length() - 1));
    }
}