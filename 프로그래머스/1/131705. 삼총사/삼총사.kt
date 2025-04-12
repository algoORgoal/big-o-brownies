import kotlin.math.pow

class Solution {
    tailrec fun dfs (selected: List<Int>, numbers: List<Int>, target: Int): Int {
        return when (selected.size) {
            0 -> {
                val candidates = 0 until numbers.size
                candidates.sumOf { dfs(selected + it, numbers, target) }
            }
            in 1..2 -> {
                val lastIndex = selected[selected.size - 1]
                val candidates = lastIndex + 1 until numbers.size
                candidates.sumOf { dfs(selected + it, numbers, target) }
            }
            else -> {
                val sum = selected.sumOf { numbers[it] }
                if (sum == target) 1 else 0
            }
        }
    }
    fun solution(numbers: IntArray): Int {
        return dfs(emptyList<Int>(), numbers.toList(), 0)
    }
}