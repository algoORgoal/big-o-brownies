class Solution {
    fun solution(arr: IntArray, divisor: Int): IntArray {
        return arr.filter { it % divisor == 0 }.sorted().let { if (it.size == 0) listOf(-1) else it }.toIntArray()
    }
}