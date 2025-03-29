import kotlin.math.min
import kotlin.math.ceil

class Solution {
    fun createBoxList(boxList: List<List<Int>>, total: Int, current: Int, width: Int, isReversed: Boolean): List<List<Int>> {
        if (current >= total) return boxList
        
        val next = current + width
        val row = next.let {
            if (next > total && isReversed) List(next - total) { 0 } + (total downTo current + 1).toList()
            else if (next <= total && isReversed) (next downTo current + 1).toList()
            else if (next > total && !isReversed) (current + 1..total).toList()
            else if (next <= total && !isReversed) (current + 1..next).toList()
            else throw Exception("error")
        }
        return createBoxList(boxList + listOf(row), total, next, width, !isReversed)
    }
    
    
    fun solution(n: Int, w: Int, num: Int): Int {
        val boxList = createBoxList(emptyList<List<Int>>(), n, 0, w, false)
        
        var x: Int = 0
        var y: Int = 0
        for (i in 0..boxList.size - 1) {
            for (j in 0..boxList[i].size - 1) {
                if (boxList[i][j] == num) {
                    x = i
                    y = j
                }
            }
        }
        
        var count: Int = 0
        for (level in x..boxList.size - 1) {
            if (boxList.getOrNull(level)?.getOrNull(y) == null || boxList.getOrNull(level)?.getOrNull(y) == 0) break
            count += 1
        }
        return count
    }
}