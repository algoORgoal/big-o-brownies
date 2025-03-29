class Solution {
    fun getBoxCountToRemove(boxCount: Int, width: Int, current: Int): Int {
        val next = current + (2 * width) - 1
        if (next > boxCount) return 1
        else return 1 + getBoxCountToRemove(boxCount, width, next)
    }
    
    
    fun solution(n: Int, w: Int, num: Int): Int {
        return getBoxCountToRemove(n, w, num)
    }
}