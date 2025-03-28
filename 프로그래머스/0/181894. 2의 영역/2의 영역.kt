class Solution {
    fun solution(arr: IntArray): IntArray {
        if (!(2 in arr)) return listOf(-1).toIntArray()
        val start = arr.toList().indexOfFirst { it == 2 }
        val last = arr.toList().indexOfLast { it == 2 }
        return arr.slice(start..last).toIntArray()
    }
}