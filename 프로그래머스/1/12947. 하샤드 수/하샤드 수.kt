class Solution {
    fun solution(x: Int): Boolean {
        val sum = x.toString().sumOf { it.toString().toInt() }
        return when (x % sum) {
            0 -> true
            else -> false
        }
    }
}