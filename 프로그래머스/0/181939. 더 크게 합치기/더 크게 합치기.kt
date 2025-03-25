class Solution {
    fun solution(a: Int, b: Int): Int {
        val first = (a.toString() + b.toString()).toInt()
        val second = (b.toString() + a.toString()).toInt()
        if (first >= second) return first
        else return second
    }
}