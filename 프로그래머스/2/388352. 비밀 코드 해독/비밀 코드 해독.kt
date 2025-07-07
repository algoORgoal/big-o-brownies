class Solution {
    fun combination(n: Int, k: Int, current: Set<Int>, max: Int): List<Set<Int>> {
        if (current.size == k) return listOf(current)
        val range = if (current.isEmpty()) 1..n else max+1..n
        return range.fold(emptyList()) { acc, element ->
            if (element in current) acc
            else acc + combination(n, k, current + element, element)
        }
    }
    
    
    fun solution(n: Int, q: Array<IntArray>, ans: IntArray): Int {
        val lists = combination(n, 5, emptySet(), 0)
        
        return lists.filter { set -> 
            q.withIndex().all { (index, query) ->
                query.filter { number -> number in set }.size == ans[index]
            } 
        }.size
        return 0
    }
}

// 30C5 = 142506
