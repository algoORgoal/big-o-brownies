class Solution {
    fun solution(myStr: String): Array<String> {
        val arr = myStr.split("[a-c]".toRegex()).filter { !it.isEmpty() }
        if (arr.isEmpty()) return arrayOf("EMPTY")
        return arr.toTypedArray()
    }
}