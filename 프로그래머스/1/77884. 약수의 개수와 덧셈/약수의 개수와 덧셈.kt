import kotlin.math.sqrt

class Solution {
    fun solution(left: Int, right: Int): Int {
        val sum = (left..right).fold(0) { acc, element ->
            val sqrtElement = sqrt(element.toDouble()).toInt()
            val divisorCount = (1..sqrtElement).sumOf<Int> {
                when {
                    (element % it) != 0 -> 0
                    (element / it) == it -> 1
                    else -> 2
                }.toInt()
            }
            
            when (divisorCount % 2) {
                0 -> acc + element
                else -> acc - element
            }
        }
        return sum
    }
}