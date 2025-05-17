class Solution {
    fun solution(strings: Array<String>, n: Int): Array<String> {
        return strings.toList().sortedWith(Comparator<String> { string1, string2 -> 
            string1[n] - string2[n] 
        }.thenComparing { string1, string2 ->
            when {
                string1 < string2 -> -1
                else -> 1
            } 
        }).toTypedArray()
    }
}