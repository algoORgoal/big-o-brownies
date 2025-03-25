class Solution {
    fun solution(arr: IntArray, delete_list: IntArray): IntArray {
        val filteredArray: IntArray = arr.filter {
            if (it in delete_list) false
            else true
        }.toIntArray()
        return filteredArray
    }
}