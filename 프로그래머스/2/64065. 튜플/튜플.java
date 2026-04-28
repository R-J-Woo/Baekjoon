import java.util.*;

class Solution {
    public int[] solution(String s) {
        
        String[] arr = s.split(",|\\{|\\}");
        Map<Integer, Integer> map = new HashMap<>();
        
        for (String a : arr) {
            if (!a.isEmpty()) {
                int num = Integer.parseInt(a);
                map.put(num, map.getOrDefault(num, 0) + 1);
            }
        }
        
        List<Integer> keySet = new ArrayList<>(map.keySet());
        keySet.sort((a, b) -> map.get(b) - map.get(a));
        
        int[] answer = new int[keySet.size()];
        for (int i = 0; i < keySet.size(); i++) {
            answer[i] = keySet.get(i);
        }
        
        return answer;
    }
}