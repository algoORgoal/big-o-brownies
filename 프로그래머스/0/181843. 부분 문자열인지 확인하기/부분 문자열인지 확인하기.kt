class Solution {
    fun solution(my_string: String, target: String): Int {
        if (target in my_string) return 1
        else return 0
    }
}