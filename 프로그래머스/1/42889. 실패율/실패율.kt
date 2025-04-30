// 각 스테이지 별로 도전자 수를 mapping table로 저장
// 스테이지 n의 실패율 = 스테이지에 머무르는 플레이어 수 / 스테이지에 도달한 플레이어 수
// 각 스테이지에 머무르는 플레이어 수를 mapping table로 관리한다.
// 스테이지에 도달한 플레이어 수는 (각 스테이지에 머무르는 플레이어 수)에 대해 postfix sum으로 구한다.

class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        val table = stages.fold(mutableMapOf<Int, Int>()) { acc, stage ->
            acc[stage] = (acc[stage] ?: 0) + 1
            acc
        }.toSortedMap()
        
        val postfixSumList = ((N + 1) downTo 1).fold(emptyList<Int>()) { acc, element -> 
            val sum = (table[element] ?: 0) + (acc.getOrNull(0) ?: 0)
            listOf(sum) + acc
        }
        val probabilities = postfixSumList.mapIndexed { index, element ->
            if (element == 0) 0.toDouble()
            else (table[index + 1] ?: 0)  / element.toDouble()
        }.slice(0 until postfixSumList.size - 1)
        
        return probabilities
            .mapIndexed { index, probability -> probability to (index + 1) }
            .sortedByDescending { it.first }
            .map { it.second }
            .toIntArray()
    }
}