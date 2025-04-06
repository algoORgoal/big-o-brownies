// 각 수의 약수의 개수를 구하기 -> sqrt(100,000)^2
// 제곱근까지만 세서 약수의 개수를 셀 수 있다.
// 약수의 개수가 limit보다 크다 -> power 반환하기
// 약수의 개수가 limit보다 작거나 같다 -> 약수의 개수 반환하기

import kotlin.math.sqrt

class Solution {
    fun solution(number: Int, limit: Int, power: Int): Int {
        return (1..number).sumOf { target ->
            val targetSqrt = sqrt(target.toDouble()).toInt()
            val divisorCount = (1..targetSqrt).fold(0) { acc, candidate ->
                when {
                    candidate * candidate == target -> acc + 1
                    target % candidate == 0 -> acc + 2
                    else -> acc
                }
            }
            when {
                divisorCount <= limit -> divisorCount
                else -> power
            }
        }
    }
}