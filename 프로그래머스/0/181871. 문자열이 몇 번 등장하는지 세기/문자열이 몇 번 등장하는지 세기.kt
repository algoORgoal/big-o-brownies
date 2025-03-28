class Solution {
    fun solution(myString: String, pat: String): Int {
        return myString.windowed(pat.length).filter { it == pat }.size
    }
}