class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n; i++) {
            int total = 0;
            for (int j = i; j <= n; j++) {
                total += j;
                
                if (total == n) {
                    answer += 1;
                    break;
                } else if (total > n) {
                    break;
                }
            }
        }
        
        return answer;
    }
}