class Solution {
    fun solution(a: Int, b: Int): Long {
        return when (a < b) {
            true -> (a.toLong()..b.toLong()).sum()
            else -> (b.toLong()..a.toLong()).sum()
        }
    }
}