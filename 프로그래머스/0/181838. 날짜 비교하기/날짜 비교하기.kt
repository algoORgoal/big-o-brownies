class Solution {
    fun solution(date1: IntArray, date2: IntArray): Int {
        val (year1, month1, day1) = date1
        val (year2, month2, day2) = date2
        return when {
            (year1 != year2) -> if (year1 < year2) 1 else 0
            else -> {
                when {
                    (month1 != month2) -> if (month1 < month2) 1 else 0
                    else -> {
                        when {
                            day1 < day2 -> 1
                            else -> 0
                        }
                    }
                }
            }
        }
    }
}