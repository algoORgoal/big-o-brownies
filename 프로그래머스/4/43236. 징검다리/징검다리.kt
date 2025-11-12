import java.util.PriorityQueue

class Solution {
    fun solution(distance: Int, rocks: IntArray, n: Int): Int {
        val pq = PriorityQueue<Map<String, Int>>(Comparator { a, b -> 
            if (a["distance"]!! == b["distance"]!!) {
                a["nextDistance"]!! - b["nextDistance"]!!
            } else {
                a["distance"]!! - b["distance"]!!
            }
        })
        
        val sortedRocks = rocks.sorted()
        val distances = sortedRocks.foldIndexed(emptyList<Int>()) { index, acc, position ->
            val lastPosition = if (index == 0) 0 else sortedRocks[index - 1]
            val distance = position - lastPosition
            acc + distance
        }.let { distances ->
            val lastDistance = distance - sortedRocks.last()
            distances + lastDistance
        }
        
        val distanceMap = mutableMapOf<Int, Int>()
        
        distances.forEachIndexed { index, distance ->
            val nextIndex = index + 1
            val nextDistance = if (index + 1 == distances.size) n else distances[index + 1]
            val node = mapOf("index" to index + 1, "nextIndex" to nextIndex + 1, "prevIndex" to index - 1, "distance" to distance)
            pq.add(node)
            distanceMap[index + 1] = distance
        }
        
        println(pq)
        println(distanceMap)
        
    
        val distanceSet = (1..distances.size).toMutableSet()
        println(distanceSet)
        
        for (i in 0 until n) {
            // val node = pq.remove()
            // val updatedIndex = node.distance + node.nextDistance
            
            // println(node)
        }
        
        return 0
    }
}

// 바위, 거리, 다음 바위, 다음 바위 거리
// 0 2 11 14 17 21 25
// 바위: 1, 거리: 2, 다음 바위: 2, 다음 바위 거리: 9, 이전 바위: 0
// 바위: 5, 거리: 4 다음 바위: 6, 다음 바위 거리: 4, 이전 바위: 4
// 1. 바위 제거
// 2. 노드 insert: 바위 2, 거리 11, 다음 바위: 3, 다음 바위 거리: 3
// 비교 순위: 1. 거리 작은 순 2. 다음 바위 거리 작은 순
// 필터:
// 현재, 이전, 다음 바위 중 하나가 제거되었으면 skip
// 이전 바위 제거가 되었을 경우 현재 거리가 outdated
// 현재 바위가 제거되었을 경우 다음에 insert하는 노드의 다음 바위 거리가 outdated
// 다음 바위가 제거되었을 경우 다음에 insert하는 노드의 현재 바위 정보 자체가 outdated