class Solution {
    public int[] solution(long n) {
        String st = "" + n;
        int[] answer = new int[st.length()];
        int index = 0;
        
        while(n > 0) {
            answer[index] = (int)(n % 10);
                
            n /= 10;
            
            index += 1;
        }
        
        return answer;
    }
}