class Solution {
    fun solution(n: Int, lost: IntArray, extra: IntArray): Int {
        val unaffectStudentCount = n - lost.size
        val recoverableStudentCount = lost.toSet().intersect(extra.toSet()).size
        val shareable = extra.toSet() - lost.toSet()
        val helped = (lost.toSet() - extra.toSet()).toMutableSet()
        
        val helpedStudentCount = shareable.toSortedSet().toList().fold(0) { acc, uniform ->
            when {
                (uniform - 1) in helped -> {
                    helped.remove(uniform - 1)
                    acc + 1
                }
                (uniform + 1) in helped -> {
                    helped.remove(uniform + 1)
                    acc + 1
                }
                else -> acc
            }
        }
        
        return unaffectStudentCount + helpedStudentCount + recoverableStudentCount
    }
}