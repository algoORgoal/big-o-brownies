class Solution {
    fun solution(numList: IntArray): Int {
        val evenSum = numList.toList().chunked(2) { it[0] }.sum()
        val oddSum = numList.toList().chunked(2) { it.getOrElse(1) { 0 } }.sum()
        if (evenSum > oddSum) return evenSum
        else return oddSum
    }
}