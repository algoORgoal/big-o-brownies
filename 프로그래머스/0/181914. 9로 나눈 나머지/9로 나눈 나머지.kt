class Solution {
    fun solution(number: String): Int {
        val sum = number.fold(0) { acc, char -> acc + char.toString().toInt() }
        return sum % 9
    }
}