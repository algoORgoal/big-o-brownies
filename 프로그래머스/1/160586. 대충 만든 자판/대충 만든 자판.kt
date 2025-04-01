// 각 문자별로 키를 눌러야 하는 최소 횟수 저장
// 문자별 최소 횟수의 합 = 문자열을 작성하는데 필요한 최소 횟수

class Solution {
    fun solution(keymap: Array<String>, targets: Array<String>): IntArray {
        val requiredTypingTable = keymap.fold(mutableMapOf<Char, Int>()) { acc, str ->
            str.mapIndexed { index, char ->
                val typingCount = index + 1
                if (acc[char] == null) acc[char] = typingCount
                else if (acc[char]?.let { it > typingCount } ?: false) acc[char] = typingCount
            }
            acc
        }
        return targets.map { target ->
            if (target.any { requiredTypingTable[it] == null }) -1
            else target.sumOf { requiredTypingTable[it] ?: 0 }
        }.toIntArray()
    }
}