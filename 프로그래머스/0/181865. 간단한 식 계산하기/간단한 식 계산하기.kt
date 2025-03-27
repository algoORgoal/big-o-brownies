class Solution {
    fun solution(binomial: String): Int {
        val (numStr1, op, numStr2) = binomial.split(" ")
        val num1 = numStr1.toInt()
        val num2 = numStr2.toInt()
        return when (op) {
            "+" -> num1 + num2
            "-" -> num1 - num2
            else -> num1 * num2
        }
    }
}