class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        val sortedSizes = sizes.map { it.toList().sorted() }
        val maxWidth = sortedSizes.maxOf { it.first() }
        val maxHeight = sortedSizes.maxOf { it.last() }
        return maxWidth * maxHeight
    }
}