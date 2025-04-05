// k번째번째 원소까지 순회할 때 문자 -> 가장 마지막 위치 인덱스의 mapping table 저장
// k + 1번째 문자가 없을 경우 -1 저장, 문자가 table에 있을 경우 k - table[char]를 저장

class Solution {
    fun solution(s: String): IntArray {
        val nearbyIndices = mutableListOf<Int>()
        s.foldIndexed(mutableMapOf<Char, Int>()) { index, acc, char -> 
            if (char in acc) nearbyIndices.add(index - (acc[char] ?: 0))
            else nearbyIndices.add(-1)
            acc[char] = index
            acc
        }
        return nearbyIndices.toIntArray()
    }
}