class Solution {
    fun solution(n: Int, control: String): Int {
        return control.fold(n) { acc, command -> 
            acc + when (command) {
                'w' -> 1
                's' -> -1
                'd' -> 10
                else -> -10
            } 
        }
    }
}