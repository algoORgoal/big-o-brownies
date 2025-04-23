class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        return absolutes.toList().zip(signs.toList()).fold(0) { acc, (value, direction) ->
            when (direction) {
                true -> acc + value
                else -> acc - value
            }
        }
        
    }
}