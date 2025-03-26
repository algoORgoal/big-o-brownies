class Solution {
    fun solution(numList: IntArray, n: Int): IntArray {
        return (numList.slice(n until numList.size) + numList.slice(0 until n)).toIntArray()
    }
}