class Solution {
    fun solution(str1: String, str2: String): String {
        return str1.zip(str2).fold("") {
            acc, (char1, char2) ->
            acc + char1 + char2
        }
    }
}