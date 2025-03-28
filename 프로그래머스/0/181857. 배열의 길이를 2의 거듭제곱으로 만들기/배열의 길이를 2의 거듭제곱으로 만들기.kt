import kotlin.math.log2;
import kotlin.math.ceil;
import kotlin.math.pow;

class Solution {
    fun solution(arr: IntArray): IntArray {
        val exponential = ceil(log2(arr.size.toDouble())).toInt()
        
        return arr + IntArray(2.toDouble().pow(exponential).toInt() - arr.size) { 0 }
    }
}