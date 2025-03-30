class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        val start = park.let { matrix ->
            val x = matrix.indexOfFirst { row -> 'S' in row }
            val y = matrix[x].indexOf('S')
            x to y
        }
        
        val (matrix, last) = routes.foldIndexed(park to start) { index, acc, route ->
            val (matrix, current) = acc
            val (x, y) = current
            val (op, distanceStr) = route.split(" ")
            val distance = distanceStr.toInt() + 1
            
            val path = when (op) {
                "N" -> List(distance) { x - it to y }
                "S" -> List(distance) { x + it to y }
                "W" -> List(distance) { x to y - it }
                else -> List(distance) { x to y + it }
            }
            val isPathValid = path.all { (x, y) -> if (matrix.getOrNull(x)?.getOrNull(y) != null && matrix.getOrNull(x)?.getOrNull(y) != 'X') true else false }
            
            if (isPathValid) {
                val next = path.last()
                matrix to next
            }
            else matrix to current
        }
        return last.toList().toIntArray()
    }
}