class Solution {
    fun solution(n: Int, lost: IntArray, extra: IntArray): Int {
        val lostUniformSet = lost.toMutableSet()
        val extraUniformSet = extra.toMutableSet()
        
        val recoverableStudentCount = extra.fold(0) { acc, extraUniform ->
            if (extraUniform in lostUniformSet) {
                lostUniformSet.remove(extraUniform)
                extraUniformSet.remove(extraUniform)
                acc + 1
            }
            else {
                acc
            }
        }
        
        val compensableStudentCount = extraUniformSet.toSortedSet().fold(0) { acc, extraUniform -> 
            when {
                (extraUniform - 1) in lostUniformSet -> {
                    lostUniformSet.remove(extraUniform - 1)
                    acc + 1
                }
                (extraUniform + 1) in lostUniformSet -> {
                    lostUniformSet.remove(extraUniform + 1)
                    acc + 1
                }
                else -> acc
            }
        }
        
        val unaffectedStudentCount = n - lost.size
        val coveredStudentCount = recoverableStudentCount + compensableStudentCount + unaffectedStudentCount
        
        return coveredStudentCount
    }
}