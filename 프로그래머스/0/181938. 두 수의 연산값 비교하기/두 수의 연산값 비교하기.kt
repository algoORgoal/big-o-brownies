class Solution {
    fun solution(a: Int, b: Int): Int {
        val first = (a.toString() + b.toString()).toInt()
        val second = 2 * a * b
        if (first >= second) return first
        else return second
    }
}