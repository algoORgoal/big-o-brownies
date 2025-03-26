class Solution {
    fun solution(my_string: String, is_prefix: String): Int {
        if (my_string.startsWith(is_prefix)) return 1
        else return 0
    }
}