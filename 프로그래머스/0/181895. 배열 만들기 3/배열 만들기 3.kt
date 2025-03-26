class Solution {
    fun solution(arr: IntArray, intervals: Array<IntArray>): IntArray {
       return intervals.flatMap { (start, end) -> arr.slice(start..end) }.toIntArray()
    }
}