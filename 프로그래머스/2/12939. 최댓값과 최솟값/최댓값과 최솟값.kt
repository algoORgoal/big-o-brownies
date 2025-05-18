import kotlin.math.max
import kotlin.math.min

class Solution {
    fun solution(s: String): String {
        val numberStringList = s.split(" ")
        val maxNumber = numberStringList.map { it.toInt() }.maxOrNull() ?: 0
        val minNumber = numberStringList.map { it.toInt() }.minOrNull() ?: 0
        return "${minNumber} ${maxNumber}"
    }
}