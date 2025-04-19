class Solution {
    fun solution(sizes: Array<IntArray>): Int {
        return sizes.map { it.toList().sorted() }.let { sortedSizes ->
            sortedSizes.maxOf { it.first() } * sortedSizes.maxOf { it.last() }
        }
    }
}