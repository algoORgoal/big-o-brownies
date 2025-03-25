class Solution {
    fun solution(strArr: Array<String>): Array<String> {
        return strArr.filter { !("ad" in it) }.toTypedArray()
    }
}