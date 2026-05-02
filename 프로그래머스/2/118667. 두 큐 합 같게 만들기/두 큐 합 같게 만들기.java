import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int n = queue1.length;
        int[] arr = new int[n * 2];
        
        long total = 0;
        
        // 배열 합치기
        for (int i = 0; i < n; i++) {
            arr[i] = queue1[i];
            arr[i + n] = queue2[i];
            total += queue1[i] + queue2[i];
        }
        
        // 전체 합이 홀수면 불가능
        if (total % 2 != 0) return -1;
        
        long target = total / 2;
        
        // 투 포인터
        int left = 0, right = n;
        long sum = 0;
        
        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }
        
        int count = 0;
        int limit = n * 4; // 충분한 상한
        
        while (count <= limit) {
            if (sum == target) return count;
            
            if (sum < target) {
                sum += arr[right % (2 * n)];
                right++;
            } else {
                sum -= arr[left % (2 * n)];
                left++;
            }
            
            count++;
        }
        
        return -1;
    }
}