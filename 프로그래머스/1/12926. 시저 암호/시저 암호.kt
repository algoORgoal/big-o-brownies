class Solution {
    fun solution(s: String, n: Int): String {
        
        return s.map { character ->
            val characterCount = 'z' - 'a' + 1
            when (character) {
                in ('a'..'z') -> {
                    val offset = character - 'a'
                    'a' + ((offset + n) % characterCount)
                }
                in ('A'..'Z') -> {
                    val offset = character - 'A'
                    'A' + ((offset + n) % characterCount)
                }
                else -> character
            }
        }.joinToString("")
    }
}

