// 날짜를 dayTime(일로 따진 시간)으로 변환
// 년 = year * 12 * 28, 달 = hour * 28
// 각 terms를 파싱해서 mapping table 만들기. 약관 종류 -> 유효기간 dayTime
// 각 privacies에 대해 파기해야되면(오늘 날짜 > 유효기한) index + 1 반환

class Solution {
    fun getDaytime(date: String): Int {
        val (yearStr, monthStr, dayStr) = date.split('.')
        return yearStr.toInt() * 12 * 28 + monthStr.toInt() * 28 + dayStr.toInt()
    }
    
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        val todayDaytime = getDaytime(today)
        val table = terms.fold(mutableMapOf<String, Int>()) { acc, term ->
            val (type, month) = term.split(" ")
            acc[type] = getDaytime("00.$month.00") - 1
            acc
        }
        
        val expiredPrivacies = privacies.foldIndexed(emptyList<Int>()) { index, acc, privacy ->
            val (dateStr, type) = privacy.split(" ")
            val daytime = getDaytime(dateStr)
            val validUntil = daytime + (table[type] ?: 0)
            if (todayDaytime > validUntil) acc + (index + 1)
            else acc
        }
        return expiredPrivacies.toIntArray()
    }
}