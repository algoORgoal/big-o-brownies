class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        queries.forEach {
            (s, e) ->
            (s..e).forEach { index -> arr[index] += 1 }
        }
        return arr
    }
}