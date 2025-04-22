class Solution {
    tailrec fun convert(acc: String, s: String): String {
        if (s.length == 0) return acc
        val numbers = mapOf<String, Int>("zero" to 0, "one" to 1, "two" to 2, "three" to 3, "four" to 4, "five" to 5, "six" to 6, "seven" to 7, "eight" to 8, "nine" to 9)
        val matched = numbers.asSequence().firstNotNullOfOrNull { (str, num) -> 
            when {
                s.startsWith(str) -> str 
                s.startsWith(num.toString()) -> num.toString()
                else -> null
            }
        }       
        
        return convert(acc + (numbers[matched] ?: matched), s.drop(matched!!.length))
    }
    
    fun solution(s: String): Int {
        return convert("", s).toInt()
    }
}