class Solution {
    fun solution(intStrs: Array<String>, k: Int, s: Int, l: Int): IntArray {
        return intStrs.fold(emptyList<Int>()) {
            acc, str ->
            val num = str.slice(s..s+l-1).toInt()
            if (num > k) acc + num
            else acc
        }.toIntArray()
    }
}