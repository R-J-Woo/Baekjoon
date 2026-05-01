import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // 1. 문자열로 변환
        String[] arr = new String[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            arr[i] = String.valueOf(numbers[i]);
        }
        
        // 2. 정렬 (핵심)
        Arrays.sort(arr, (a, b) -> (b + a).compareTo(a + b));
        
        // 3. 결과 합치기
        StringBuilder sb = new StringBuilder();
        for (String s : arr) {
            sb.append(s);
        }
        
        // 4. 예외 처리 (0000 → 0)
        if (sb.charAt(0) == '0') return "0";
        
        return sb.toString();
    }
}