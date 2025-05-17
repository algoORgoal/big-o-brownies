class Solution {
    fun solution(n: Int): String {
        return (1..n).map { index ->
            when (index % 2) {
                1 -> '수'
                else -> '박'
            }
        }.joinToString("")
    }
}