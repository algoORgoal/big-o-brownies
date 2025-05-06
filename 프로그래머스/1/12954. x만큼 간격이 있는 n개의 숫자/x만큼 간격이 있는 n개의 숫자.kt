class Solution {
    fun solution(x: Int, n: Int): LongArray {
        return generateSequence(x.toLong()) { it + x }.take(n).toList().toLongArray()
    }
}