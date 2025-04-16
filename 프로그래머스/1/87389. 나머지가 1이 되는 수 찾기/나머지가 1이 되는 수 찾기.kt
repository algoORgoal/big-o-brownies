class Solution {
    fun solution(n: Int): Int {
        return (1..n).find { n % it == 1 } ?: 0
    }
}