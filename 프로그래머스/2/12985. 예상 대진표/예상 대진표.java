class Solution
{
    private int nxt_num(int num) {
        int nxt = 0;
        if (num % 2 == 1) {
            num++;
        } 
        
        return num / 2;
    }
    
    public int solution(int n, int a, int b)
    {
        int answer = 0;
        
        while (true) {
            answer += 1;
            
            // 서로 만나게 된다면 중지
            if (Math.abs(a - b) == 1 && Math.min(a, b) % 2 == 1) {
                break;
            }
            
            a = nxt_num(a);
            b = nxt_num(b);
        }

        return answer;
    }
}