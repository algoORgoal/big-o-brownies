class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        return a.zip(b).sumOf { (element1, element2) ->
            element1 * element2
        }
    }
}