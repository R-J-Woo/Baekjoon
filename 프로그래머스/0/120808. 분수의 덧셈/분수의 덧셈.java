class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        
        int under = denom1 * denom2;
        int top = denom1 * numer2 + denom2 * numer1;
        
        int max = 1;
        for (int i = 1; i <= Math.min(under, top); i++) {
            if (under % i == 0 && top % i == 0) {
                max = i;
            }
        }
        
        return new int[] { top / max, under / max };
    }
}