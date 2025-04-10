class Solution {
    fun solution(n: Int, slicer: IntArray, numList: IntArray): IntArray {
        return slicer.let { (a, b, c) -> 
            when (n) {
                1 -> numList.slice(0..b)
                2 -> numList.slice(a until numList.size)
                3 -> numList.slice(a..b)
                else -> numList.slice(a..b step c)
            }.toIntArray()
        }
    }
}