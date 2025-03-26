class Solution {
    fun solution(numList: IntArray): Int {
        return numList.indexOfFirst { it < 0 }
    }
}