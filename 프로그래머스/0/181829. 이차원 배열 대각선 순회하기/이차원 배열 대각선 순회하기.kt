class Solution {
    fun solution(board: Array<IntArray>, k: Int): Int {
        val filteredBoard = board.indices.map {
            i ->
            board[i].filterIndexed {
                j, num -> 
                i + j <= k
            }
        }
        return filteredBoard.fold(0) {
            acc, row ->
            acc + row.sum()
        }
    }
}