import kotlin.math.abs

class Solution {
    fun solution(survey: Array<String>, choices: IntArray): String {
        val pairs = survey.toList().zip(choices.toList())
        val table = pairs.fold(mutableMapOf<Char, Int>()) { acc, (type, answer) ->
            val score = answer - 4
            when {
                score < 0 -> acc[type[0]] = (acc[type[0]] ?: 0) + abs(score)
                score > 0 -> acc[type[1]] = (acc[type[1]] ?: 0) + abs(score)
            }
            acc
        }
        return listOf('R' to 'T', 'C' to 'F', 'J' to 'M', 'A' to 'N').fold("") { acc, (type1, type2) ->
            when {
                (table[type1] ?: 0) >= (table[type2] ?: 0) -> acc + type1
                else -> acc + type2
            }
        }
    }
}