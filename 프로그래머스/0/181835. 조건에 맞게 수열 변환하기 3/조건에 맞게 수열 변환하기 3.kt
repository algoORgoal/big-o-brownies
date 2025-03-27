class Solution {
    fun solution(arr: IntArray, k: Int): IntArray {
        if (k % 2 == 1) {
            return arr.map { it * k }.toIntArray()
        } else {
            return arr.map { it + k }.toIntArray()
        }
    }
}