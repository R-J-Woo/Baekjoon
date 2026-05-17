import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            queue.add(priorities[i]);
        }
        
        while (true) {
            int value = queue.poll();
            
            // 우선순위가 높은게 따로 있으면 뒤에 추가
            if (!queue.isEmpty() && value < Collections.max(queue)) {
                queue.offer(value);
            } else {
                answer++;
                
                if (location == 0) {
                    break;
                }
            }
            
            // location 옮겨주기
            if (location > 0) {
                location--;
            } else {
                location = queue.size() - 1;
            }
        }
        
        return answer;
    }
}