// 각 스테이지 별로 도전자 수를 mapping table로 저장
// 스테이지 n의 실패율 = 스테이지에 머무르는 플레이어 수 / 스테이지에 도달한 플레이어 수
// 각 스테이지에 머무르는 플레이어 수를 mapping table로 관리한다.
// 스테이지에 도달한 플레이어 수는 (각 스테이지에 머무르는 플레이어 수)에 대해 postfix sum으로 구한다.

class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        // 각 스테이지에 머무르는 플레이어 수
        val table = stages.fold(mutableMapOf<Int, Int>()) { acc, stage ->
            acc[stage] = (acc[stage] ?: 0) + 1
            acc
        }.toSortedMap()
        
        // 각 스테이지에 도달한 플레이어 수
        val postfixSumTable = ((N + 1) downTo 1).fold(mutableMapOf<Int, Int>()) { acc, element -> 
            val sum = (table[element] ?: 0) + (acc[element + 1] ?: 0)
            acc[element] = sum
            acc
        }.toSortedMap()
        
        val probabilities = postfixSumTable.entries.map { (stage, count) ->
            stage to when (count) {
                0 -> 0.toDouble()
                else -> (table[stage] ?: 0)  / count.toDouble()
            }
        }.slice(0 until postfixSumTable.size - 1)
        return probabilities.sortedByDescending { it.second }.map { it.first }.toIntArray()
        
    }
}