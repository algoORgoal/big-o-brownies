// 빈 병 20병을 가져갔을 때 
// 빈 병의 개수
// 10 + 5 + 2 + 1 = 19
// 빈 병 n병을 가져갔을 때
// 받을 수 있는 병의 개수
// (n/a) * b


class Solution {
    tailrec fun computeBottleCount(a: Int, b: Int, current: Int, sum: Int, left: Int): Int {
        if (current < a) {
            if (current + left >= a) return computeBottleCount(a, b, current + left, sum, 0)
            else return sum + (left / a) * b
        }
        val next = (current / a) * b
        val extra = current % a
        return computeBottleCount(a, b, next, sum + next, left + extra)
    }
    
    fun solution(a: Int, b: Int, n: Int): Int {
        return computeBottleCount(a, b, n, 0, 0)
    }
}