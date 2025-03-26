class Solution {
    fun solution(num_list: IntArray, n: Int): IntArray {
        return num_list.toList().chunked(n) { it[0] }.toIntArray()
    }
}