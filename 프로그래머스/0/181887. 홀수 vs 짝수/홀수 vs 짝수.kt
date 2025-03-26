class Solution {
    fun solution(numList: IntArray): Int {
        val evenSum = numList.filterIndexed { index, num -> index % 2 == 0 }.sum()
        val oddSum = numList.filterIndexed { index, num -> index % 2 == 1 }.sum()
        if (evenSum > oddSum) return evenSum
        else return oddSum
    }
}