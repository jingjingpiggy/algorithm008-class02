class Solution {
    public String reverseOnlyLetters(String S) {
        char[] arr = S.toCharArray();
        int len = arr.length, l = -1, r = len;
        if (len < 2) return s

        while (l++ < r--) {
            while (l < r && !valid(arr[l])) l++;
            while (l < r && !valid(arr[r])) r--;
            if ( l < r ) {
                arr[l] ^= arr[r];
                arr[r] ^= arr[l];
                arr[l] ^= arr[r];
            }
        }
        return new String(arr);
    }
}

private boolean valid(char c) {
    return (c >= 'a' && c<= 'z') || (c >= 'A' && c<= 'Z')
}
