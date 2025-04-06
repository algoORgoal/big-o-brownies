// 현재 첫 글자 x, x가 나온 횟수, x가 나오지 않은 횟수

class Solution {
    fun solution(s: String): Int {
        var count: Int = 0
        val a = object {
            var firstCharacter: Char? = null
            var firstCharacterIndex: Int? = null
            var firstCharacterCount: Int? = null
            var otherCharacterCount: Int? = null
        }
        s.forEachIndexed { index, char ->
            when {
                a.firstCharacter == null -> {
                    a.firstCharacter = char
                    a.firstCharacterIndex = index
                    a.firstCharacterCount = 1
                    a.otherCharacterCount = 0
                }
                char == a.firstCharacter -> a.firstCharacterCount?.let{
                    a.firstCharacterCount = it + 1
                }
                char != a.firstCharacter -> a.otherCharacterCount?.let{
                    a.otherCharacterCount = it + 1
                }
            }
            a.firstCharacterCount?.let { firstCharacterCount ->
                a.otherCharacterCount?.let { otherCharacterCount ->
                    if (firstCharacterCount == otherCharacterCount || index == s.length - 1) {
                        count += 1
                        a.firstCharacter = null
                        a.firstCharacterIndex = null
                        a.firstCharacterCount = null
                        a.otherCharacterCount = null
                    }
                }
            }
        }
        return count
    }
}