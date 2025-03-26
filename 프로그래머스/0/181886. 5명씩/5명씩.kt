class Solution {
    fun solution(names: Array<String>): Array<String> {
        return names.toList().chunked(5) { it[0] }.toTypedArray()
    }
}