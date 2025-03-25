import kotlin.math.abs
import kotlin.math.pow

class Solution {
    fun solution(a: Int, b: Int): Int {
        return when ((a % 2) + (b % 2)) {
            2 -> (a.toDouble().pow(2) + b.toDouble().pow(2)).toInt()
            1 -> 2 * (a + b)
            0 -> abs(a - b)
            else -> 0
        }
    }
}