class Solution {
    fun solution(myString: String, pat: String): String {
        return myString.slice(0 until myString.lastIndexOf(pat)) + pat
    }
}