class Solution {
    fun solution(n: Long): IntArray {
        return n.toString().toList().reversed().map { it.toString().toInt() }.toIntArray()
    }
}