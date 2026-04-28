import java.util.*;

class Solution {
    public int solution(String dirs) {
        int x = 0, y = 0;
        int answer = 0;
        
        Set<String> set = new HashSet<>();
        
        for (char d : dirs.toCharArray()) {
            int nx = x, ny = y;
            
            if (d == 'U') ny++;
            else if (d == 'D') ny--;
            else if (d == 'R') nx++;
            else if (d == 'L') nx--;
            
            // 범위 벗어나면 무시
            if (nx < -5 || nx > 5 || ny < -5 || ny > 5) continue;
            
            // 경로 (양방향 모두 저장)
            String path1 = x + "," + y + "->" + nx + "," + ny;
            String path2 = nx + "," + ny + "->" + x + "," + y;
            
            if (!set.contains(path1)) {
                set.add(path1);
                set.add(path2);
                answer++;
            }
            
            x = nx;
            y = ny;
        }
        
        return answer;
    }
}