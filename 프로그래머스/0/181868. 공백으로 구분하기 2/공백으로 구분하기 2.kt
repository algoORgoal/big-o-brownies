class Solution {
    fun solution(my_string: String): Array<String> {
        val chunks = my_string.trim().split("\\s+".toRegex())
        return chunks.toTypedArray()
    }
}