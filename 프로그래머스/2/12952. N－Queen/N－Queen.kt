class Solution {
    fun backtracking(n: Int, currentRow: Int, visitedColumns: MutableSet<Int>, visitedLeftDiagonals: MutableSet<Int>, visitedRightDiagonals: MutableSet<Int>): Int {
        if (currentRow == n) {
            return 1
        }
        
        var caseCount = 0
        for (i in 0..(n - 1)) {
            if (i in visitedColumns || (currentRow - i) in visitedLeftDiagonals || (currentRow + i) in visitedRightDiagonals) {
                continue
            } else {
                visitedColumns.add(i)
                visitedLeftDiagonals.add(currentRow - i)
                visitedRightDiagonals.add(currentRow + i)
                caseCount += backtracking(n, currentRow + 1, visitedColumns, visitedLeftDiagonals, visitedRightDiagonals)
                visitedColumns.remove(i)
                visitedLeftDiagonals.remove(currentRow - i)
                visitedRightDiagonals.remove(currentRow + i)
            }
        }
        return caseCount
    }
    
    
    
    fun solution(n: Int): Int {
        val visitedRows = mutableSetOf<Int>()
        val visitedLeftDiagonals = mutableSetOf<Int>()
        val visitedRightDiagonals = mutableSetOf<Int>()
        return backtracking(n, 0, visitedRows, visitedLeftDiagonals, visitedRightDiagonals)
    }
}