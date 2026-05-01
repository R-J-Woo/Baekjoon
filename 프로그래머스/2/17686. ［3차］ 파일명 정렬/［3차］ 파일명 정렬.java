import java.util.*;

class Solution {
    
    static class FileInfo {
        String original;
        String head;
        int number;
        
        public FileInfo(String original, String head, int number) {
            this.original = original;
            this.head = head;
            this.number = number;
        }
    }
    
    public String[] solution(String[] files) {
        List<FileInfo> list = new ArrayList<>();
        
        for (String file : files) {
            int idx = 0;
            
            // HEAD 추출
            while (idx < file.length() && !Character.isDigit(file.charAt(idx))) {
                idx++;
            }
            String head = file.substring(0, idx);
            
            // NUMBER 추출
            int start = idx;
            while (idx < file.length() && Character.isDigit(file.charAt(idx)) && idx - start < 5) {
                idx++;
            }
            int number = Integer.parseInt(file.substring(start, idx));
            
            list.add(new FileInfo(file, head, number));
        }
        
        // 정렬
        Collections.sort(list, (a, b) -> {
            // HEAD 비교 (대소문자 무시)
            int headCompare = a.head.toLowerCase().compareTo(b.head.toLowerCase());
            if (headCompare != 0) return headCompare;
            
            // NUMBER 비교
            return a.number - b.number;
        });
        
        // 결과 반환
        String[] answer = new String[files.length];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i).original;
        }
        
        return answer;
    }
}