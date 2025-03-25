import kotlin.math.pow

class Solution {
    fun solution(numList: IntArray): Int {
        val product = numList.fold(1) { acc, num -> acc * num }
        val product2 = numList.sum().toDouble().pow(2).toInt()
        if (product < product2) return 1
        else return 0
    }
}