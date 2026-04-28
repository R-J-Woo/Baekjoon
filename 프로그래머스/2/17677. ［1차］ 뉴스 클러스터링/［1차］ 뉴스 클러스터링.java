import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        
        List<String> list1 = makeList(str1.toLowerCase());
        List<String> list2 = makeList(str2.toLowerCase());
        
        Map<String, Integer> map1 = makeMap(list1);
        Map<String, Integer> map2 = makeMap(list2);
        
        Set<String> keys = new HashSet<>();
        keys.addAll(map1.keySet());
        keys.addAll(map2.keySet());
        
        int intersection = 0;
        int union = 0;
        
        for (String key : keys) {
            int a = map1.getOrDefault(key, 0);
            int b = map2.getOrDefault(key, 0);
            
            intersection += Math.min(a, b);
            union += Math.max(a, b);
        }
        
        // 둘 다 공집합이면
        if (union == 0) return 65536;
        
        return (int) ((double) intersection / union * 65536);
    }
    
    // 2글자씩 끊기 + 필터링
    private List<String> makeList(String s) {
        List<String> list = new ArrayList<>();
        
        for (int i = 0; i < s.length() - 1; i++) {
            char a = s.charAt(i);
            char b = s.charAt(i + 1);
            
            if (Character.isLetter(a) && Character.isLetter(b)) {
                list.add("" + a + b);
            }
        }
        
        return list;
    }
    
    // 빈도 맵 만들기
    private Map<String, Integer> makeMap(List<String> list) {
        Map<String, Integer> map = new HashMap<>();
        
        for (String s : list) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }
        
        return map;
    }
}