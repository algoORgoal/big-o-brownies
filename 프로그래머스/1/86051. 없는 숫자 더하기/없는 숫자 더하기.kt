class Solution {
    fun solution(numbers: IntArray): Int {
        return (0..9).filter { !(it in numbers) }.sum()
    }
}