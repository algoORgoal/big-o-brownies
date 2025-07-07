class Solution {
    tailrec fun gcd(a: Int, b: Int): Int {
        return when {
            a < b -> gcd(b, a) 
            b == 0 -> a
            else -> gcd(b, a % b)
        }
    }
    
    fun lcd(a: Int, b: Int): Int {
        return a * b / gcd(a, b)
    }
    
    fun solution(arr: IntArray): Int {
        return arr.fold(1) { acc, element -> lcd(acc, element) }
    }
}
