class Solution {
    fun solution(citations: IntArray): Int {
        for (i in 1..10000) {
            val citationCount = citations.count { it >= i }
            if (citationCount < i) return i - 1
        }
        return 10000
    }
}