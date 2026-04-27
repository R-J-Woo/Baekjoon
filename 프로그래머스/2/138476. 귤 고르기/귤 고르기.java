import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        // 귤 크기별 개수
        Map<Integer, Integer> map = new HashMap<>();
        for (int num:tangerine) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        
        // 개수만 리스트로 추출
        List<Integer> counts = new ArrayList<>(map.values());
        
        // 내림차순 정렬
        counts.sort(Collections.reverseOrder());
        
        int sum = 0;
        for (int count:counts) {
            sum += count;
            answer++;
            if (sum >= k) {
                break;
            }
        }
        
        return answer;
    }
}