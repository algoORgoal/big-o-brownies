class Solution {
    fun solution(arr: IntArray): IntArray {
        return arr.withIndex().minByOrNull { (index, element) -> element }?.let { (minIndex, minElement) ->
            (arr.slice(0 until minIndex) + arr.slice(minIndex + 1 until arr.size)).toIntArray() 
        }?.let {            
            when (it.size) {
                0 -> listOf(-1).toIntArray()
                else -> it
            }
        } ?: listOf(-1).toIntArray()
    }
}