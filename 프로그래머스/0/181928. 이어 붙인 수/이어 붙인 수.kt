class Solution {
    fun solution(numList: IntArray): Int {
        val oddString = numList.fold("") {
            acc, num ->
            if (num % 2 == 1) acc + num.toString()
            else acc
        }
        val evenString = numList.fold("") {
            acc, num ->
            if (num % 2 == 0) acc + num.toString()
            else acc
        }
        return oddString.toInt() + evenString.toInt()
    }
}