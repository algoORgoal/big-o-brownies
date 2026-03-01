class Solution {
    fun solution(n: Int, results: Array<IntArray>): Int {
        var graph = results.fold(mutableMapOf<Int, MutableList<Int>>()) { acc, result ->
            val (source, destination) = result
            
            if (!(source in acc))
                acc[source] = mutableListOf<Int>()
            acc[source]?.add(destination)
            acc
        }    
        
        var reversedGraph = results.fold(mutableMapOf<Int, MutableList<Int>>()) { acc, result ->
            val (source, destination) = result
            
            if (!(destination in acc))
                acc[destination] = mutableListOf<Int>()
            acc[destination]?.add(source)
            acc
        }
        
        val descendantsMap = mutableMapOf<Int, Set<Int>>()
        val ancestorsMap = mutableMapOf<Int, Set<Int>>()
        
        for (i in (1..n)) {
            if (i !in descendantsMap) {
                dfs(i, graph, descendantsMap)
            }
            if (i !in ancestorsMap) {
                dfs(i, reversedGraph, ancestorsMap)
            }
        }
        
//         println(descendantsMap)
//         println(ancestorsMap)
        
        var count = 0
        for (i in (1..n)) {
            if (descendantsMap[i]!!.size + ancestorsMap[i]!!.size == n - 1) {
                count += 1
            }
        }
        
        return count
    }
    
    fun dfs(current: Int, graph: MutableMap<Int, MutableList<Int>>, descendantsMap: MutableMap<Int, Set<Int>>) {
        if (current in graph) {
            descendantsMap[current] = emptySet<Int>()
            
            for (adjacent_node in graph[current]!!) {
                if (adjacent_node in descendantsMap) {
                    
                    descendantsMap[current] = descendantsMap[current]!! + descendantsMap[adjacent_node]!!
                    descendantsMap[current] = descendantsMap[current]!! + adjacent_node
                    continue
                }
                dfs(adjacent_node, graph, descendantsMap)
                descendantsMap[current] = descendantsMap[current]!! + descendantsMap[adjacent_node]!!
                descendantsMap[current] = descendantsMap[current]!! + adjacent_node
            }
        } else {
            descendantsMap[current] = emptySet<Int>()
        }
    }
}


// 노드: 1 ~ n
// 정확하게 순위를 매길 수 있음 => 위상정렬 가능 => DAG
// 단, 위상정렬 시에서는 edge의 왼쪽 => 오른쪽 순서만 보장
// 정확하게 순위 매길 수 있는지 확인하기 위해서는 조상 개수 + 자손 개수 = n - 1
// 위상정렬이 아닌, dfs를 통해서 확인
// dfs를 통한 자손 개수 확인하는 방법: set() union 연산을 통해 해결. DAG는 자손 중에 겹치는 노드 있음
// 부모 개수 확인: edge 반전시켜서 확인
// 시간복잡도: O(n + m)
// 공간복잡도: O(n + m) (graph)
// 4 => 3 => 2 => 5
// 4 => 2
// 1 => 2 => 5

