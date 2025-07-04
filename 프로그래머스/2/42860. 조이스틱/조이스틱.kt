import kotlin.math.abs
import kotlin.math.min

class Solution {
    fun countMove(name: String, currentIndex: Int, count: Int, trial: Int): Int {
        val newName = name.slice(0 until currentIndex) + 'A' + name.slice(currentIndex + 1 until name.length)
        val currentMoveCount = min(abs(name[currentIndex] - 'A'), abs(name[currentIndex] - 'Z') + 1)
        
        if (newName.all { it == 'A' }) return count + currentMoveCount
        
        var left = if (currentIndex == 0) name.length - 1 else currentIndex - 1
        var leftMoveCount = 1
        while (name[left] == 'A') {
            left = if (left == 0) name.length - 1 else left - 1
            leftMoveCount += 1
        }
        
        var right = (currentIndex + 1) % name.length
        var rightMoveCount = 1
        while (name[right] == 'A') {
            right = (right + 1) % name.length
            rightMoveCount += 1
        }
        
        
        return Math.min(countMove(newName, left, count + currentMoveCount + leftMoveCount, trial + 1), countMove(newName, right, count + currentMoveCount + rightMoveCount, trial + 1))
    }
    
    fun solution(name: String): Int {
        return countMove(name, 0, 0, 0)
    }
}


// 5 0
// 5 1 => 4
// 5 2 => 3
// 5 3 => 2
// 5 4 => 1
// 5 5 => 0
// 5 6 => -1 => 9
// 5 7 => -2 => 8
// 5 8 => -3 => 7
// 5 9 => -4 => 6
// 5 10 => -5 => 5
// 5 11 => -6 => 4
// 5 12 => -7 => 3
// 5 13 => -8 => 2
// 5 14 => -9 => 1
// 5 15 => -10 => 0
// 5 16 => -11 => 9


// length - (right % currentIndex)
// 10 - (6 % 5)
// 10 - (1 % 5) 