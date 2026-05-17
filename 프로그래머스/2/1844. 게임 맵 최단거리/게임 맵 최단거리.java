import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        
        Queue<int[]> queue = new LinkedList<>();
        int row = maps.length;
        int col = maps[0].length;
        boolean[][] visited = new boolean[row][col];
        
        queue.offer(new int[] {0, 0, 1}); // x좌표, y좌표, 이동한 칸의 수
        visited[0][0] = true;
        
        int[] dx = new int[] {-1, 1, 0, 0};
        int[] dy = new int[] {0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] arr = queue.poll();
            int x = arr[0];
            int y = arr[1];
            int count = arr[2];
            
            if (x == row - 1 && y == col - 1) {
                answer = count;
                break;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (0 <= nx && nx < row && 0 <= ny && ny < col && maps[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[] {nx, ny, count + 1});
                }
            }
        }
        
        return answer;
    }
}