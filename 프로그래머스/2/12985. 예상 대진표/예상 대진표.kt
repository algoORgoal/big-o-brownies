import kotlin.math.abs
import kotlin.math.ceil

class Solution {
    tailrec fun countRound(a: Int, b: Int, roundCount: Int): Int {
        return when {
            a - b == 1 && b % 2 == 1 -> roundCount
            b - a == 1 && a % 2 == 1 -> roundCount
            else -> {
                countRound(ceil(a.toDouble() / 2).toInt(), ceil(b.toDouble() / 2).toInt(), roundCount + 1)
            }
        }
    }
    
    fun solution(n: Int, a: Int, b: Int): Int {
        return countRound(a, b, 1)
    }
}