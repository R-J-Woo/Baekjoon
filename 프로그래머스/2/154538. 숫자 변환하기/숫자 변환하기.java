import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = -1;
        
        Queue<int[]> queue = new LinkedList<>();
        boolean[] visited = new boolean[y + 1];
        
        queue.offer(new int[]{x, 0}); // 시작 X와 연산횟수 count
        visited[x] = true;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int node = cur[0];
            int count = cur[1];
            
            if (node == y) {
                answer = count;
                break;
            }
            
            if (node + n <= y && !visited[node + n]) {
                visited[node + n] = true;
                queue.offer(new int[]{node + n, count + 1});
            }
            if (node * 2 <= y && !visited[node * 2]) {
                visited[node * 2] = true;
                queue.offer(new int[]{node * 2, count + 1});
            }
            if (node * 3 <= y && !visited[node * 3]) {
                visited[node * 3] = true;
                queue.offer(new int[]{node * 3, count + 1});
            }
        }
        
        return answer;
    }
}