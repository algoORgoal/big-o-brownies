class Solution {
    fun solution(s: String): IntArray {
        val trimmedString = s.slice(1 until s.length - 1)
        val sequenceList = Regex("\\{([0-9]+,)*[0-9]+\\}").findAll(trimmedString).fold(emptyList<List<Int>>()) { acc, element ->
            val value = element.value
            acc + listOf(value.slice(1 until value.length - 1).split(',').map { it.toInt() })
        }
        val table = sequenceList.fold(mutableMapOf<Int, Int>()) { acc, sequence -> 
            sequence.forEach { acc[it] = (acc[it] ?: 0) + 1 }
            acc
        }
        return table.toList().sortedWith(Comparator<Pair<Int, Int>> { a, b -> b.second - a.second }).map { it.first }.toIntArray()
    }
}

// 1. [0-9]+
// 2. [0-9]+,[0-9]+, [0-9]+

// String을 파싱하여, String -> List<Set<Int>>로 변환
// 해당 List를 Set의 length 순으로 오름차순 정렬
// fold를 사용하여 각 집합별로 가장 마지막에 있는 원소를 추가