class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder sb = new StringBuilder();
        
        int num = 0;
        
        // 1. 충분한 길이까지 n진수 문자열 생성
        while (sb.length() < t * m) {
            sb.append(Integer.toString(num, n).toUpperCase());
            num++;
        }
        
        // 2. 튜브가 말할 문자 추출
        StringBuilder answer = new StringBuilder();
        
        for (int i = p - 1; i < t * m; i += m) {
            answer.append(sb.charAt(i));
            if (answer.length() == t) break;
        }
        
        return answer.toString();
    }
}