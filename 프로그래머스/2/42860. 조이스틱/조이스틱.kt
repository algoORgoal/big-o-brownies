import kotlin.math.abs
import kotlin.math.min

class Solution {
    fun countMove(name: String, currentIndex: Int, count: Int, trial: Int): Int {
        val newName = name.slice(0 until currentIndex) + 'A' + name.slice(currentIndex + 1 until name.length)
        val currentMoveCount = min(abs(name[currentIndex] - 'A'), abs(name[currentIndex] - 'Z') + 1)
        
        if (newName.all { it == 'A' }) return count + currentMoveCount
        
        var left = currentIndex
        var leftMoveCount = 0
        while (newName[left] == 'A') {
            left = if (left == 0) newName.length - 1 else left - 1
            leftMoveCount += 1
        }
        
        var right = currentIndex
        var rightMoveCount = 0
        while (newName[right] == 'A') {
            right = (right + 1) % newName.length
            rightMoveCount += 1
        }
        
        
        return Math.min(countMove(newName, left, count + currentMoveCount + leftMoveCount, trial + 1), countMove(newName, right, count + currentMoveCount + rightMoveCount, trial + 1))
    }
    
    fun solution(name: String): Int {
        return countMove(name, 0, 0, 0)
    }
}


// 더 먼 것을 선택했을 경우, 돌아오는 과정에서 더 많은 코스트가 소요된다.
// k + 1 까지 최적 선택
// greedy는 더 먼 것을 선택했으므로, 돌아오는 과정에서 같거나 더 많은 코스트 소요
// 시간복잡도: 20(string length, 전부 'A'인지 확인) * 2^20(각 문자별로 왼쪽, 오른쪽 확인)