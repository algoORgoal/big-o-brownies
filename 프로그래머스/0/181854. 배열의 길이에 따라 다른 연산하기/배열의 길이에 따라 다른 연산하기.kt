class Solution {
    fun solution(arr: IntArray, n: Int): IntArray {
        if (arr.size % 2 == 1)
            return arr.mapIndexed {
                index, number ->
                if (index % 2 == 0) number + n
                else number
            }.toIntArray()
        else
            return arr.mapIndexed {
                index, number ->
                if (index % 2 == 1) number + n
                else number
            }.toIntArray()
    }
}