class Solution {
    fun solution(myString: String): String {
        return myString.map {
            when (it) {
                'a' -> 'A'
                'A' -> 'A'
                else -> it.lowercase()
            }
        }.joinToString("")
    }
}