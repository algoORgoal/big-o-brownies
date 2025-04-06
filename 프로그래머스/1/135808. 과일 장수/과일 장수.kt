// 가장 낮은 점수 * 개수
// 사과를 팔아서 얻을 수 있는 최대 이익
// 총 이익 계산 방식: (상자에 들어가는 사과의 개수) * (각 상자에서 점수가 가장 낮은 사과)
// 각 상자에서 점수가 가장 낮은 사과는 무엇일까?
// a k b k
// k + 1 개의 사과를 한 상자에 담는다.
// 그냥 가장 높은 것부터 담는다.

// m개가 있을 때 -> 그냥 m개 중에 낮은 거 고르니까 정답 찾는다.
// k * m개가 있을 때 -> 높은 거부터 상자에 계속 담는 게 정답이라고 하자.
// (k + 1) * m개가 있을 때 -> 정답을 찾는다.(왜?)


class Solution {
    fun solution(k: Int, m: Int, scores: IntArray): Int {
        val sortedScores = scores.sorted()
        if (sortedScores.size < m) return 0
        else {
            return sortedScores.drop(sortedScores.size % m).chunked(m).sumOf { box -> box.first() } * m
        }
    }
}

// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
