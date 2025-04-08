class Solution {
//     tailrec fun getPalindrome(foods: List<Int>, acc: String, current: Int):  {
        
//     }
    fun solution(foods: IntArray): String {
        return foods.reversed().foldIndexed("0") { index, acc, count ->
            val type = foods.size - index - 1
            when {
                index == foods.size - 1 -> acc
                else -> {
                    val round = type.toString().repeat(count / 2)
                    round + acc + round
                }
            }
        }
    }
}