class Solution {
    fun solution(n: Int): Array<IntArray> {
        return (1..n).mapIndexed {
            i, _index1 ->
            (1..n).mapIndexed {
                j, _index2 ->
                if (i == j) 1
                else 0
            }.toIntArray()
        }.toTypedArray()
    }
}