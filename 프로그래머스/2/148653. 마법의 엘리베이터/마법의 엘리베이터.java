class Solution {
    public int solution(int storey) {
        int answer = 0;
        
        while (storey > 0) {
            int digit = storey % 10;
            int next = (storey / 10) % 10;
            
            if (digit > 5) {
                // 올림
                answer += (10 - digit);
                storey += 10;
                
            } else if (digit < 5) {
                // 내림
                answer += digit;
                
            } else { // digit == 5
                if (next >= 5) {
                    answer += 5;
                    storey += 10;
                } else {
                    answer += 5;
                }
            }
            
            storey /= 10;
        }
        
        return answer;
    }
}