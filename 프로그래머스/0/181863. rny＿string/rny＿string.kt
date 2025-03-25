class Solution {
    fun solution(rny_string: String): String {
        val modifiedString = rny_string.fold("") {
            acc, char ->
            if (char == 'm') acc + "rn"
            else acc + char
        }
        return modifiedString
    }
}