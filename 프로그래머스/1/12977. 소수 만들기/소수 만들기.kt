import java.math.BigInteger
import kotlin.math.sqrt
import kotlin.math.pow
import kotlin.math.max

class Solution {
    fun isPrime(num: Int): Boolean {
        return (2..sqrt(num.toDouble()).toInt()).none { num % it == 0 }
    }
    
    fun combination(nums: List<Int>, part: List<Int>): Int {
        return when {
            part.size == 3 -> if (isPrime(part.sumOf { nums[it] })) 1 else 0
            part.size == 0 -> {
                (0 until nums.size).sumOf { index ->
                    combination(nums, part + index)
                }
            }
            else -> {
                val largestIndex = part.last()
                (largestIndex + 1 until nums.size).sumOf { index ->
                    combination(nums, part + index)
                }
            }
        }
    }
    
    fun solution(nums: IntArray): Int {
        return combination(nums.toList(), emptyList<Int>())
    }
}