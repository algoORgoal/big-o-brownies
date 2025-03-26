class Solution {
    fun solution(my_strings: Array<String>, parts: Array<IntArray>): String {
        return my_strings.zip(parts).fold("") { acc, (str, part) -> acc + str.slice(part[0]..part[1]) }
    }
}