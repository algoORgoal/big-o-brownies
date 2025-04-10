class Solution {
    fun canProunce(babbling: String, lastWord: String): Boolean {
        if (babbling.length == 0) return true
        val words = listOf<String>("aya", "ye", "woo", "ma")
        val matchingWord = words.find { word -> babbling.startsWith(word) }
        return when (matchingWord) {
            null -> false
            lastWord -> false
            else -> canProunce(babbling.slice(matchingWord.length until babbling.length), matchingWord)
        }
    }
    
    
    fun solution(babbling: Array<String>): Int {
        return babbling.filter { canProunce(it, "") }.size
    }
}