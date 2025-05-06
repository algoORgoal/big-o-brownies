class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        return (0 until arr1.size).map { i ->
            (0 until arr1[i].size).map { j ->
                arr1[i][j] + arr2[i][j]
            }.toIntArray()
        }.toTypedArray()
    }
}