class Solution {
    fun solution(n: Int): Int {
        return when (n) {
            0 -> 0
            1 -> 1
            else -> {
                val (a, b) = (2..n).foldIndexed(0 to 1) { index, (a, b), element ->
                    when (index % 2) {
                        0 -> ((a + b) % 1234567 to b)
                        else -> (a to (b + a) % 1234567)
                    }
                }
                when (n % 2) {
                    0 -> a
                    else -> b
                }
            } 
        }
    }
}