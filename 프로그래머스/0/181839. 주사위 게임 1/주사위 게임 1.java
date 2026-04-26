class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int count = 0;
        if (a % 2 == 1) {
            count += 1;
        }
        if (b % 2 == 1) {
            count += 1;
        }
        
        if (count == 2) {
            answer = ((int) Math.pow(a, 2) + (int) Math.pow(b, 2));
        }
        else if (count == 1) {
            answer = 2 * (a + b);
        }
        else {
            answer = Math.abs(a - b);
        }
        
        return answer;
    }
}