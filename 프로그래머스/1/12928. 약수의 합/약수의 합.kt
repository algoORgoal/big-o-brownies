class Solution {
    fun solution(n: Int): Int {
        return (1..n).filter { element -> if (n % element == 0) true else false }.sum()
    }
}