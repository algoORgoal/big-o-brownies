class Solution {
    tailrec fun countCases(target: Int, current: Int, memo: MutableMap<Int, Long>): Long {
        when (current) {
            0 -> {
                memo[current] = 1
            } 
            1 -> {
                memo[current] = 1
            }
            else -> {
                memo[current] = (memo[current - 1] ?: 0) + (memo[current - 2] ?: 0) 
            }
        }
        memo[current] = (memo[current] ?: 1) % 1234567
        
        return when (current) {
            target -> memo[current] ?: 0
            else -> countCases(target, current + 1, memo)
        }
    }
    
    fun solution(n: Int): Long {
        return countCases(n, 0, mutableMapOf<Int, Long>())
    }
}