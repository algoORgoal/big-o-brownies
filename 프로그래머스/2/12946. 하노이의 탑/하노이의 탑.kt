// f(1, 3, n)
// = f(1, 2, n - 1) + [1, 3]
//   + f(2, 1, n - 1) + [2, 3]
//   + f(1, 2, n - 2) + [1, 3]

class Solution {
    fun getOrder(source: Int, other: Int, destination: Int, count: Int): List<Pair<Int, Int>> {
        return when (count) {
            1 -> listOf(source to destination)
            else -> getOrder(source, destination, other, count - 1) + listOf(source to destination) + getOrder(other, source, destination, count - 1)
        }
    }
    
    fun solution(n: Int): Array<IntArray> {
        val order = getOrder(1, 2, 3, n)
        return order.map { (from, to) -> listOf(from, to).toIntArray() }.toTypedArray()
    }
}