class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        val start = park.let { matrix ->
            val x = matrix.indexOfFirst { row -> 'S' in row }
            val y = matrix[x].indexOf('S')
            x to y
        }
        
        val last = routes.foldIndexed(start) { index, current, route ->
            val (x, y) = current
            val (op, distanceStr) = route.split(" ")
            val distance = distanceStr.toInt() + 1
            
            val path = when (op) {
                "N" -> List(distance) { x - it to y }
                "S" -> List(distance) { x + it to y }
                "W" -> List(distance) { x to y - it }
                else -> List(distance) { x to y + it }
            }
            val isPathValid = path.all { (x, y) -> if (park.getOrNull(x)?.getOrNull(y) != null && park.getOrNull(x)?.getOrNull(y) != 'X') true else false }
            
            if (isPathValid) {
                val next = path.last()
                next
            }
            else current
        }
        return last.toList().toIntArray()
    }
}