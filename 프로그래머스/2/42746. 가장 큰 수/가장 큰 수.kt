class Solution {
    fun solution(numbers: IntArray): String {
        if (numbers.all { it == 0 }) { 
            return "0"
        }
        return numbers.sortedWith { a, b -> 
            val ab = "$a$b".toInt()
            val ba = "$b$a".toInt()
            ba.compareTo(ab)
        }.fold("") { acc, element ->
            acc + element.toString()
        }
    }
}

// a, b
// 정렬 순서: ab가 더 큰지, ba가 더 큰지 비교