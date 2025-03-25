class Solution {
    fun solution(arr: IntArray): IntArray {
        return arr.flatMap { element ->  List(element) { element } }.toIntArray()
    }
}