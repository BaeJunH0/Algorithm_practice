import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(long i = 100000000; i >= 1; i /= 10) {
            answer += n / i;
            
            if(n / i != 0) {
                n -= n / i * i;
            }
        }
        return answer;
    }
}