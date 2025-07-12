class Solution {
    fun combination(string: String, current: Int = 0): List<String> {
        if (current == string.length) return listOf("")
        val excludedSubsets = combination(string, current + 1)
        val includedSubsets = excludedSubsets.map { subset ->
            string[current] + subset
        }
        return excludedSubsets + includedSubsets
    }
    
    fun solution(orders: Array<String>, course: IntArray): Array<String> {
        val courseSet = course.toSet()
        val satisfiedSubsets = orders.flatMap {
            combination(it.toList().sorted().joinToString(""))
        }.filter { it.length in courseSet }
        val subsetTable = satisfiedSubsets.groupingBy { it }.eachCount().toList().groupBy { it.first.length }
        val mostFrequentStrings = subsetTable.flatMap { (length, list) ->
            val maxOccurence = list.maxOfOrNull { it.second } ?: 0
            list.filter { (string, occurence) ->
                occurence > 1 && occurence == maxOccurence
            }.map { it.first }
        }
        return mostFrequentStrings.sorted().toTypedArray()        
    }
}

// 1. 각각의 단품메뉴 조합으로 낼 수 있는 course[0], ...개 조합 뽑기 => 최대 10C1 + 10C2 + ... + 10C10 = 2^10 = 1024
// 2. 출현빈도 세기 => 1024
// 3. 길이별로 묶어서 가장 빈도가 높은 것들 추려내기 => 1024