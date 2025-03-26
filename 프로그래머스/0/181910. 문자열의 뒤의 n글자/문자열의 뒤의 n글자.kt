class Solution {
    fun solution(my_string: String, n: Int): String {
        return my_string.slice(my_string.length - n until my_string.length)
    }
}