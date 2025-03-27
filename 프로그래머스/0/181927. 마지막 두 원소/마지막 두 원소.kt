class Solution {
    fun solution(numList: IntArray): IntArray {
        if (numList.last() > numList[numList.size - 2]) return numList + (numList.last() - numList[numList.size - 2])
        else return numList + (numList.last() * 2)
    }
}