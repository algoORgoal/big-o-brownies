class Solution {
    fun solution(price: Int, money: Int, count: Int): Long {
        return generateSequence(price.toLong()) { it + price }.take(count).sum().let {
            if (money >= it) 0 else it - money
        }
    }
}