class Solution {
    fun solution(s: String): String {
        return s.toList().sortedWith(Comparator { char1, char2 -> 
            when {
                char1 in ('a'..'z') && char2 in ('A'..'Z') -> -1
                char1 in ('A'..'Z') && char2 in ('a'..'z') -> 1
                else -> char2 - char1
            }
        }).joinToString("")
    }
}