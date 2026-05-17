import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        Queue<int[]> queue = new LinkedList<>();
        // queue에 현재값, 들어간 정수의 개수 저장
        queue.offer(new int[] {numbers[0], 1});
        queue.offer(new int[] {-1 * numbers[0], 1});
        
        while (!queue.isEmpty()) {
            int[] arr = queue.poll();
            int value = arr[0];
            int count = arr[1];
            
            // 이미 모든 정수를 사용했다면
            if (count == numbers.length) {
                if (value == target) {
                    answer++;
                }
                continue;
            }
            
            queue.offer(new int[] {value + numbers[count], count + 1});
            queue.offer(new int[] {value - numbers[count], count + 1});
        }
        
        return answer;
    }
}