// 15와 20의 최대공약수
// 3 * 5 | 2 * 2 * 5
// 20, 15 -> 15, 5 -> 5 0 => 5
// 10 3 => 3 1 => 1 0 => 1
class Solution {
    fun gcd(n: Int, m: Int): Int {
        return when {
            n < m -> gcd(m, n)
            m == 0 -> n
            else -> gcd(m, n % m)
        }
    }
    
    fun lcm(n: Int, m: Int): Int {
        return (n * m) / gcd(n, m)
    }
    
    fun solution(n: Int, m: Int): IntArray {
        val a = gcd(n, m)
        val b = lcm(n, m)
        return listOf(a, b).toIntArray()
    }
}

