class Solution {
    fun solution(myString: String): Array<String> {
        val strList = myString.split("x").filter { it != "" }
        return strList.sorted().toTypedArray()
    }
}