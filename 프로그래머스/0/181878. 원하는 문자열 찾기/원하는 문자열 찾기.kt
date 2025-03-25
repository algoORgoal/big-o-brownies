class Solution {
    fun solution(myString: String, pat: String): Int {
        if (myString.contains(pat, ignoreCase = true)) return 1
        else return 0
    }
}