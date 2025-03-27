class Solution {
    fun solution(a: Int, d: Int, included: BooleanArray): Int {
        return included.withIndex().sumOf {
            (index, bool) ->
            if (bool) a + d * index
            else 0
        }
    }
}