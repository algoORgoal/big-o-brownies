class Solution {
    fun solution(numLog: IntArray): String {
        return numLog.toList().windowed(size = 2).fold("") { 
            acc, pair ->
            val difference = pair[1] - pair[0]
            if (difference == 1) acc + 'w'
            else if (difference == -1) acc + 's'
            else if (difference == 10) acc + 'd'
            else acc + 'a'
        }
    }
}