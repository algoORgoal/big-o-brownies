class Solution {
    fun solution(names: Array<String>, yearnings: IntArray, photos: Array<Array<String>>): IntArray {
        val table = names.toList().zip(yearnings.toList()).map { (name, yearning) -> name to yearning }.toMap()
        return photos.map { photo ->
            photo.sumOf { table[it] ?: 0 }
        }.toIntArray()
    }
}