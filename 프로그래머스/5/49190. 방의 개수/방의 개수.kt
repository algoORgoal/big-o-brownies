class Solution {
    fun move(current: Pair<Int, Int>, direction: Int): List<Pair<Int, Int>> {
        val (x, y) = current
        val next = when (direction) {
            0 -> listOf(x - 1 to y, x - 2 to y)
            1 -> listOf(x - 1 to y + 1, x - 2 to y + 2)
            2 -> listOf(x to y + 1, x to y + 2)
            3 -> listOf(x + 1 to y + 1, x + 2 to y + 2)
            4 -> listOf(x + 1 to y, x + 2 to y)
            5 -> listOf(x + 1 to y - 1, x + 2 to y - 2)
            6 -> listOf(x to y - 1, x to y - 2)
            else -> listOf(x - 1 to y - 1, x - 2 to y - 2)
        }
        return next
    }
    
    fun solution(arrows: IntArray): Int {
        val start = 0 to 0
        
        val path = arrows.fold(mutableListOf<Pair<Int, Int>>(start)) { acc, arrow ->
            val current = acc[acc.size - 1]
            val next_nodes = move(current, arrow)
            next_nodes.forEach { acc.add(it) }
            acc
        }
        
        val nodes = path.toSet()
        
        val disjointSet = DisjointSet(nodes)
        val visitedEdges = mutableSetOf<List<Pair<Int, Int>>>()
    
        var current = 0 to 0
        var count = 0
        
        val comparator = Comparator<Pair<Int, Int>> { a, b ->
            if (a.first != b.first) {
                a.first - b.first
            } else {
                a.second - b.second
            }
        }
        
        for (node in path) {
            if (node == current) {
                continue
            }
            
            val edge = listOf(current, node).sortedWith(comparator)
            
            if (edge !in visitedEdges && disjointSet.find(current) == disjointSet.find(node)) {
                count += 1
            }
            
            visitedEdges.add(edge)
            disjointSet.union(current, node)
            current = node
        }
        
        
        return count
    }
}

class DisjointSet(nodes: Set<Pair<Int, Int>>) {
    val parent = nodes.fold(mutableMapOf<Pair<Int, Int>, Pair<Int,Int>>()) { acc, node ->
        acc[node] = node
        acc
    }
    
    fun find(node: Pair<Int, Int>): Pair<Int, Int> {
        if (node == parent[node]!!) {
            return node
        } else {
            parent[node] = find(parent[node]!!)
            return parent[node]!!
        }
    }
    
    fun union(node1: Pair<Int, Int>, node2: Pair<Int, Int>) {
        val root1 = find(node1)
        val root2 = find(node2)
        
        if (root1 == root2) {
            return
        }
        parent[root1] = root2
    }
}


// arrows로 path 안에 있는 node들 모두 찾기
// cycle이 만들어질 때마다 += 1
// cycle 판별은 Disjoint Set으로 수행