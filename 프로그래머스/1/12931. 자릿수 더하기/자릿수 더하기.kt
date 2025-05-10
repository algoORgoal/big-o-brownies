class Solution {
    fun solution(n: Int): Int {
        return n
            .toString()
            .toList()
            .fold(0) { acc, element -> 
                acc + element
                    .toString()
                    .toInt()
            }
    }
}