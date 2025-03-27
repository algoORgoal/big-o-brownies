class Solution {
    fun solution(arr: Array<IntArray>): Int {
        val isSatisfied = arr.withIndex().all { 
            (i, row) -> 
            row.withIndex().all {
                (j, num) ->
                arr[i][j] == arr[j][i]
            }
        }
        if (isSatisfied) return 1
        else return 0
    }
}