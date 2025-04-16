class Solution {
    fun solution(n: Int): Int {
        return (1..n).first { n % it == 1 } ?: 0
    }
}