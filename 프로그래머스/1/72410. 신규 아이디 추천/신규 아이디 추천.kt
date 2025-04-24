class Solution {
    fun solution(newId: String): String {
        return newId
            .toLowerCase()
            .filter {
                when (it) {
                    in 'a'..'z' -> true
                    in '0'..'9' -> true
                    '-' -> true
                    '_' -> true
                    '.' -> true
                    else -> false
                }
            }
            .replace("[.]+".toRegex(), ".")
            .trim('.')
            .let {
                when (it.length) {
                    0 -> "a"
                    else -> it
                }
            }
            .let {
                when (it.length >= 16) {
                    true -> it.slice(0..14)
                    false -> it
                }
            }
            .let {
                when (it.endsWith('.')) {
                    true -> it.trim('.')
                    else -> it
                }
            }
            .let {
                when (it.length <= 2) {
                    true -> it.padEnd(3, it[it.length - 1])
                    else -> it
                }
            }
            
            
    }
}