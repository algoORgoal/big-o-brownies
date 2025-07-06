

class Solution {
    fun compressString(s: String, length: Int): String {
        var i = 0;
        var newString = ""
        while (i < s.length) {
            var j = i + length
            if (j + length <= s.length && s.slice(j until j + length) == s.slice(i until i + length)) {
                val word = s.slice(i until i + length)
                var wordCount = 1
                while (j + length <= s.length && s.slice(j until j + length) == word) { 
                    j += length 
                    wordCount +=1
                }
                newString += (wordCount.toString() + word)
                i = j
            } else {
                if (i + length > s.length) {
                    newString += s.slice(i until s.length)
                    break
                }
                newString += s.slice(i until i + length)
                i += length
            }
        }
        
        
        return newString
    }
    
    fun solution(s: String): Int {
        return (1..s.length).map { compressString(s, it).length }.toList().minOrNull() ?: 0   
    }
}

