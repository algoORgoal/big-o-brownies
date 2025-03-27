class Solution {
    fun solution(a: Int, b: Int, c: Int): Int {
        val numSet = setOf(a, b, c)
        val sum = a + b + c
        val squareSum = a * a + b * b + c * c 
        val cubeSum = a * a * a + b * b * b + c * c * c
        return when (numSet.size) {
            3 -> sum
            2 -> sum * squareSum
            else -> sum * squareSum * cubeSum
        }
    }
}