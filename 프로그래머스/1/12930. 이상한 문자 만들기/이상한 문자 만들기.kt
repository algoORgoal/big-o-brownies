class Solution {
    fun solution(s: String): String {
        return s
            .split(" ")
            .map { word ->
                word.mapIndexed { index, letter ->
                    when (index % 2) {
                        0 -> letter.uppercase()
                        else -> letter.lowercase()
                }
            }.joinToString("")
        }.joinToString(" ")
    }
}