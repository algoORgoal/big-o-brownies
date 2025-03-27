class Solution {
    fun solution(arr: Array<IntArray>): Int {
        val isSatisfied = arr.indices.all { 
            i -> 
            arr[i].indices.all {
                j ->
                arr[i][j] == arr[j][i]
            }
        }
        if (isSatisfied) return 1
        else return 0
    }
}