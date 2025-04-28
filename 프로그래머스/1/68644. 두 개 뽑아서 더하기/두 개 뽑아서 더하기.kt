class Solution {
    fun solution(numbers: IntArray): IntArray {
        return numbers.foldIndexed(emptySet<Int>()) { index, acc, number -> 
            val part = numbers.drop(index + 1)
            acc + part.map { it + number }
        }.toList().sorted().toIntArray()
    }
}