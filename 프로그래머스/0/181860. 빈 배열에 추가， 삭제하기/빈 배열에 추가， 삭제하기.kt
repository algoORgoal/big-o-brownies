class Solution {
    fun solution(arr: IntArray, flag: BooleanArray): IntArray {
        return arr.toList().zip(flag.toList()).fold(emptyList<Int>()) { 
            acc, (num, shouldRepeat) ->
            if (shouldRepeat) acc + (1..num * 2).toList().map { num }
            else acc.dropLast(num)
        }.toIntArray()
    }
}