import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        List<Integer> list = new ArrayList<>();
        
        int idx = 0;
        while (idx < progresses.length) {
            
            // 하루치 진도 진행
            for (int i = 0; i < progresses.length; i++) {
                progresses[i] += speeds[i];
            }
            
            int count = 0;
            for (int i = idx; i < progresses.length; i++) {
                if (progresses[i] >= 100) {
                    count += 1;
                    idx += 1;
                } else {
                    break;
                }
            }
            
            if (count > 0) list.add(count);
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}