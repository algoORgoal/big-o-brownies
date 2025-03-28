class Solution {
    fun divideUntil1(k: Int): Int {
        return when (k) {
            1 -> 0
            else -> divideUntil1(k / 2) + 1
        }
    }
    
    fun solution(numList: IntArray): Int {
        return numList.sumOf { divideUntil1(it) }
    }
}