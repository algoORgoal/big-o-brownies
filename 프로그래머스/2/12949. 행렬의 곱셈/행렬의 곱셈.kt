class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        val row = arr1.size
        val col = arr2[0].size
        val count = arr1[0].size
        val matrix = (0..row - 1).map{ (0..col - 1).toMutableList() }.toMutableList()
        for (i in 0..row - 1) {
            for (j in 0..col - 1) {
                var sum: Int = 0
                for (k in 0..count - 1) {
                    sum += arr1[i][k] * arr2[k][j]
                }
                matrix[i][j] = sum
            }
        }
        return matrix.map { it.toIntArray() }.toTypedArray()
    }
}