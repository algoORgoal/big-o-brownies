class Solution {
    fun countRequiredPaints(table: Map<Int, Int>, span: Int, current: Int): Int {
        return when {
            current > table.size -> 0
            table[current] == 0 -> 1 + countRequiredPaints(table, span, current + span)
            else -> countRequiredPaints(table, span, current + 1)
        }
    }
    
    
    fun solution(n: Int, m: Int, section: IntArray): Int {
        val pairs = section.map { it to 0 }
        val table = pairs.toMap<Int, Int>().toMutableMap().let {
            (1..n).fold(it) { acc, element ->
                if (acc[element] == null) acc[element] = 1
                acc
            }
        }.toSortedMap()
        return countRequiredPaints(table, m, 0)
    }
}