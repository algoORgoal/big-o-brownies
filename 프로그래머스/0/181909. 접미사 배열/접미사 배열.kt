class Solution {
    fun solution(my_string: String): Array<String> {
        return my_string.mapIndexed {
            index, char -> my_string.slice(index until my_string.length)
        }.sorted().toTypedArray()
    }
}