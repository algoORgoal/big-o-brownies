class Solution {
    fun solution(n_str: String): String {
        if (n_str[0] != '0') return n_str
        val from: Int = n_str.indexOfFirst { it != '0' }
        val to = n_str.length - 1
        return n_str.slice(from..to)
    }
}