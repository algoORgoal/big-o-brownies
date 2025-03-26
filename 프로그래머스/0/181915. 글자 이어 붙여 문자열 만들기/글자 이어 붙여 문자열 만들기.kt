class Solution {
    fun solution(string: String, indexList: IntArray): String {
        return indexList.fold("") { acc, index -> acc + string[index] }
    }
}