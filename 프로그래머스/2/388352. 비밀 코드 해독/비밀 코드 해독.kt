class Solution {
    fun combination(n: Int, k: Int, current: Set<Int>): List<Set<Int>> {
        if (current.size == k) return listOf(current)
        val range = ((current.maxOrNull() ?: 0) + 1)..n
        return range.fold(emptyList<Set<Int>>()) { acc, element ->
            if (element in current) acc
            else acc + combination(n, k, current + element)
        }
    }
    
    fun solution(n: Int, q: Array<IntArray>, ans: IntArray): Int {
        val lists = combination(n, 5, emptySet())
        
        return lists.count { set -> 
            q.withIndex().all { (index, query) ->
                query.count { number -> number in set } == ans[index]
            } 
        }
    }
}

// 30C5 = 142506
// 30C5 * 10 * 5
// nC5 * m * q[i] 

