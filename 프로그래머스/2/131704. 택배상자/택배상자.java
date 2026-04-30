import java.util.*;

class Solution {
    public int solution(int[] order) {
        Deque<Integer> sub = new ArrayDeque<>();
        
        int idx = 0;
        
        for (int i = 1; i <= order.length; i++) {
            // 메인 컨테이너 벨트 맨 앞의 상자가 현재 트럭에 싣는 순서라면
            if (i == order[idx]) {
                idx++;
                
                // sub에서 계속 꺼낼 수 있는지 확인
                while (!sub.isEmpty() && sub.peek() == order[idx]) {
                    sub.pop();
                    idx++;
                }
            } else {
                sub.push(i);
            }
        }
        
        // 마지막까지 sub 처리
        while (!sub.isEmpty() && sub.peek() == order[idx]) {
            sub.pop();
            idx++;
        }
        
        return idx;
    }
}