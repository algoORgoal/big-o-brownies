class Solution {
    fun solution(numList: IntArray, n: Int): IntArray {
        return numList.drop(n - 1).toIntArray()
    }
}