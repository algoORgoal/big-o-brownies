class Solution {
    fun solution(strList: Array<String>, ex: String): String {
        val filteredStrList = strList.filter { !(ex in it) }
        val joinedStr = filteredStrList.joinToString("")
        return joinedStr
    }
}