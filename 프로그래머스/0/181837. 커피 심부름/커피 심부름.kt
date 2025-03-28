class Solution {
    fun solution(order: Array<String>): Int {
        return order.sumOf {
            when {
                "americano" in it -> 4500
                "cafelatte" in it -> 5000
                else -> 4500
            }.toInt()
        }
    }
}