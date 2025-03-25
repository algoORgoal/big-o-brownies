class Solution {
    fun solution(myString: String): IntArray {
        val strings = myString.split("x".toRegex())
        println(strings)
        val stringLengths = strings.map { it.length }
        return stringLengths.toIntArray()

    }
}