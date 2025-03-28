class Solution {
    fun findFirstIndex(arr: List<Int>, count: Int): Int {
        val computedArr = compute(arr)
        if (arr == computedArr) return count
        else return findFirstIndex(computedArr, count + 1)
    }
    
    fun compute(arr: List<Int>): List<Int> {
        return arr.map { if (it >= 50 && it % 2 == 0) it / 2 else if (it < 50 && it % 2 == 1) it * 2 + 1 else it }
    }
    
    
    fun solution(arr: IntArray): Int {
        return findFirstIndex(arr.toList(), 0)
    }
}