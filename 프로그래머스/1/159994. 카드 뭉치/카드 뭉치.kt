// 모두 queue로 만들기
// target이 안 비워져 있고, deque1이나 deque2이 안 비워져 있을 동안 반복해야 한다.

class Solution {
    
    fun solution(cards1: Array<String>, cards2: Array<String>, goal: Array<String>): String {
        val deque1 = ArrayDeque(cards1.toList())
        val deque2 = ArrayDeque(cards2.toList())
        val target = ArrayDeque(goal.toList())
        while (!target.isEmpty()) {
            when {
                !deque1.isEmpty() && target.first() == deque1.first() -> {
                    target.removeFirst()
                    deque1.removeFirst()
                }
                !deque2.isEmpty() && target.first() == deque2.first() -> {
                    target.removeFirst()
                    deque2.removeFirst()
                }
                else -> return "No"
            }
        }
        return "Yes"
    }
}