class Solution {
    fun combination(list: List<Int>, currentIndex: Int, size: Int, acc: List<Int>): List<List<Int>> {
        return when (acc.size) {
            size -> listOf(acc)
            else -> {
                list.asSequence().withIndex().filter { (index, _) -> index >= currentIndex }.flatMap { (index, element) ->
                    combination(list, index + 1, size, acc + element)
                }.toList()
            }
        }
    }
    
    fun solution(relation: Array<Array<String>>): Int {
        val relationIndices = (0 until relation[0].size).toList()
        val relationList = relation.map { it.toList() }.toList()
        
        val usedSubsets = mutableListOf<Set<Int>>()
        
        val count = (1..relation[0].size).fold(0) { acc, size ->
            val subsetIndicesList = combination(relationIndices, 0, size, emptyList<Int>());
            
            val subsetCount = subsetIndicesList.map { subsetIndices ->
                val subset = relationList.map { 
                    it.filterIndexed { index, element -> index in subsetIndices } 
                }
                subsetIndices to subset
            }.count { (subsetIndices, subset) ->
                val subsetIndexSet = subsetIndices.toSet()
                if (usedSubsets.any { subsetIndexSet.containsAll(it) } == true) {
                    false
                } else {
                    val table = subset.groupingBy { it }.eachCount()
                    val isEveryKeyUnique = if (table.values.all { it == 1 }) true else false
                    if (isEveryKeyUnique) {
                        usedSubsets.add(subsetIndexSet)
                    }
                    isEveryKeyUnique    
                }
            }   
            acc + subsetCount
        }
        
        
        return count
    }
}


// C개 중에서 1개씩 뽑아, 후보키 될 수 있는지 확인 => 후보키 가능하면 리스트에서 제거하고 1 증가
// ...
// C개 중에서 C개씩 뽑아, 후보키 될 수 있는지 확인 => 후보키 가능하면 리스트에서 제거하고 1 증가
// cC1 + ... + cCc = 2^c - 1
// merge할 때마다 r번 연산 => O(r * 2^c)
// r <= 8, c <= 20: 8 * 1_000_000
// 합치는 거 어떻게 할지?
// [ 시작 인덱스, 끝 인덱스 ]를 뽑음