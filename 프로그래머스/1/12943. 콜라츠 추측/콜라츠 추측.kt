import java.math.BigInteger

class Solution {
    tailrec fun collatz(num: BigInteger, count: Int): Int {
        return when {
            num == 1.toBigInteger() -> count
            count == 500 -> -1
            num.mod(2.toBigInteger()) == 0.toBigInteger() -> collatz(num / 2.toBigInteger(), count + 1)
            else -> collatz(num * 3.toBigInteger() + 1.toBigInteger(), count + 1)
        }
    }
    
    fun solution(num: Int): Int {
        return collatz(num.toBigInteger(), 0)
    }
}