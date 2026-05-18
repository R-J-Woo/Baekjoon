import java.util.*;

class Solution {
    
    public boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, computers);
                answer++;
            }
        }
        
        return answer;
    }
    
    public void bfs(int node, int[][] computers) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        visited[node] = true;
        
        while (!queue.isEmpty()) {
            int n = queue.poll();
            for (int i = 0; i < computers[n].length; i++) {
                if (computers[n][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}