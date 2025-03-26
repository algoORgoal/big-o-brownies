class Solution {
    fun solution(arr: IntArray, target: Int): Int {
        val found = arr.withIndex().find { (index, binary) -> index >= target && binary == 1 }
        return found?.index ?: -1
    }
}