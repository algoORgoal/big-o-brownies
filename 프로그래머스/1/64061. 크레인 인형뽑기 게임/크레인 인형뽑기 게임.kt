class Solution {
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        val rowCount = board.size
        val colCount = board[0].size
        val stack = ArrayDeque<Int>()
        var popCount: Int = 0
        
        moves.forEach { move ->
            val j = move - 1
            (0 until rowCount).indexOfFirst { i -> board[i][j] != 0 }.takeIf { it >= 0 }?.let { i ->
                stack.addLast(board[i][j])
                board[i][j] = 0
            }
            
            if (stack.size >= 2 && stack.last() == stack[stack.size - 2]) {
                stack.removeLast()
                stack.removeLast()
                popCount += 2
            }
        }
        
        return popCount
    }
}