class Solution {
    fun solution(myString: String, pat: String): String {
        val lastMatchingIndex = myString.windowed(pat.length).indexOfLast { it == pat }
        return myString.slice(0 until lastMatchingIndex) + pat    
    }
}