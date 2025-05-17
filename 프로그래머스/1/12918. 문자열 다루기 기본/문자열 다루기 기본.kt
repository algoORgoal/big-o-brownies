class Solution {
    fun solution(s: String): Boolean {
        return when (s.length) {
            4, 6 -> s.all { 
                when (it) {
                    in ('0'..'9') -> true
                    else -> false
                }
            }
            else -> false
        }
    }
}