class Solution {
    fun solution(strArr: Array<String>): Int {
        val table = strArr.fold(emptyMap<Int, Int>()) { acc, str ->
            val key = str.length
            val newValue = acc[key]?.let { it + 1 } ?: 1
            acc + (key to newValue)
        }
        
        return table.maxOf { (key, value) -> value }
    }
}