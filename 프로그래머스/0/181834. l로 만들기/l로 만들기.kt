class Solution {
    fun solution(myString: String): String {
        return myString.map {
            if (it.code < 'l'.code) 'l'
            else it
        }.joinToString("")
    }
}