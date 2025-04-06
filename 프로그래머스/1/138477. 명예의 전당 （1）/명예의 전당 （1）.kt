import java.util.PriorityQueue

class Solution {
    fun solution(k: Int, scores: IntArray): IntArray {
        val (pq, lowestScores) = scores.fold(PriorityQueue<Int>() to emptyList<Int>()) { (pq, list), score -> 
            when {
                pq.size == k -> {
                    pq.add(score)
                    pq.remove()
                    pq to (list + pq.peek())
                }
                else -> {
                    pq.add(score)
                    pq to (list + pq.peek())
                }
            }
        }
        return lowestScores.toIntArray()
    }
}