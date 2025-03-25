class Solution {
    fun solution(numbers: IntArray, n: Int): Int {
        return numbers.reduce { 
            acc, num -> 
            if (acc > n) acc
            else acc + num
        }
    }
}