class Solution {
    fun solution(names: Array<String>): Array<String> {
        return names.foldIndexed(emptyList<String>()) {
            index, acc, name ->
            if (index % 5 == 0) acc + name
            else acc
        }.toTypedArray()
    }
}