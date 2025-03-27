import kotlin.math.pow;

class Solution {
    fun solution(n: Int): Int {
        if (n % 2 == 1) return (1..n).toList().filter { it % 2 == 1 }.sum()
        else return (1..n).toList().filter { it % 2 == 0 }.fold(0) { acc, num -> acc + num.toDouble().pow(2).toInt() }
    }
}