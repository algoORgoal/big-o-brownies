class Solution {
    fun solution(t: String, p: String): Int {
        return t.windowed(p.length).count { candidate -> 
            candidate.toBigInteger() <= p.toBigInteger() }
    }
}