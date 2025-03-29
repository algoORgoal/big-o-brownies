import kotlin.math.min
import kotlin.math.ceil

class Solution {
    fun solution(n: Int, w: Int, num: Int): Int {
        val boxList = (1..n)
            .chunked(w)
            .mapIndexed { index, row ->
                val missingCount = w - row.size
                when (index % 2) {
                    0 -> row + List(missingCount) { 0 }
                    1 -> List(missingCount) { 0 } + row.reversed()
                    else -> throw Exception("integer not valid")
                }
            }
            val x = boxList.indexOfFirst { num in it }
            val y = boxList[x].indexOf(num)
            return boxList.drop(x).count { it[y] != 0 }
    }
}