import kotlin.math.abs
import kotlin.math.min

class Solution {
    fun countMove(name: String): Int {
        val lastDifferentIndex = (name.length - 1 downTo 0).find { name[it] != 'A' } ?: -1
        return name.foldIndexed(0) { index, acc, element ->    
            val countFromA = abs(element - 'A')
            val countFromZ = abs(element - 'Z') + 1
            if (index > lastDifferentIndex) acc
            else if (index == 0) acc + min(countFromA, countFromZ)
            else acc + min(countFromA, countFromZ) + 1
        }
    }
    
    fun solution(name: String): Int {
        val reversedName = name[0] + name.slice(1 until name.length).reversed()
        return min(countMove(name), countMove(reversedName))
    }
}