class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        answer[0] = 0;
        answer[1] = 0;
        
        for (int num : num_list) {
            if (num % 2 == 0) {
                answer[0] += 1;
            } else {
                answer[1] += 1;
            }
        }
        
        return answer;
    }
}