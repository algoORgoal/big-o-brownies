import kotlin.math.min

class Solution {
    fun solution(X: String, Y: String): String {
        val xMap = X.fold(mutableMapOf<Char, Int>()) { acc, char ->
            acc[char] = (acc[char] ?: 0) + 1
            acc
        }.toSortedMap(Comparator.reverseOrder())
        val yMap = Y.fold(mutableMapOf<Char, Int>()) { acc, char ->
            acc[char] = (acc[char] ?: 0) + 1
            acc
        }.toSortedMap(Comparator.reverseOrder())
        val commonKeys = xMap.keys.intersect(yMap.keys)
        val commonPairs = commonKeys.associateWith { key -> min(xMap[key]!!, yMap[key]!!) }
        val string = commonPairs.toList().fold("") { acc, (char, count) -> acc + char.toString().repeat(count) }
        return when {
            string.length == 0 -> "-1"
            string.startsWith("0") -> "0"
            else -> string
        }
        
        
    }
}