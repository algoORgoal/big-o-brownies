class Solution {
    fun solution(num: Int, n: Int): Int {
        return when {
            num % n == 0 -> 1
            else -> 0
        }
    }
}