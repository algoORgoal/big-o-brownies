class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        queries.forEach {
            (i, j) ->
            arr[i] = arr[j].also { arr[j] = arr[i] }
        }
        return arr
    }
}