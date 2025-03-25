class Solution {
    fun solution(numList: IntArray): IntArray {
        return numList.sorted().slice(0..4).toIntArray()
    }
}