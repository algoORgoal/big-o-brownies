class Solution {
    fun solution(my_string: String, is_suffix: String): Int {
        if (my_string.endsWith(is_suffix)) return 1
        else return 0
    }
}