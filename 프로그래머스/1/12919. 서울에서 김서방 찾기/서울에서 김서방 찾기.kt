class Solution {
    fun solution(seoul: Array<String>): String {
        val index = seoul.indexOfFirst { it == "Kim" }
        return "김서방은 ${index}에 있다"
    }
}