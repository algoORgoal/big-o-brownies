// 현재 첫 글자 x, x가 나온 횟수, x가 나오지 않은 횟수

class Solution {
    fun solution(s: String): Int {
        var answer: Int = 0
        val stack = mutableListOf<Char>()

        s.forEach {
            if (stack.isEmpty()) {
                answer++
                stack.add(it)
            } else if (stack.first() == it) {
                stack.add(it)
            } else {
                stack.removeFirst()
            }
        }

        return answer

    }
}