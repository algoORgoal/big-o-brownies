import kotlin.math.sqrt

class Solution {
    fun solution(n: Long): Long {
        val sqrtValue = sqrt(n.toDouble()).toLong()
        return when (sqrtValue * sqrtValue) {
            n -> (sqrtValue + 1) * (sqrtValue + 1)
            else -> -1
        }
    }
}