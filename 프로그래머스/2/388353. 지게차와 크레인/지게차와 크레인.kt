class Solution {
    fun bfs(matrix: List<List<Char>>, current: Pair<Int, Int>, table: MutableMap<Char, MutableSet<Pair<Int, Int>>>, visited: MutableSet<Pair<Int, Int>>): Unit {
        if (current in visited) return
        visited.add(current)
        
        val (i, j) = current
        
        listOf(i - 1 to j, i + 1 to j, i to j - 1, i to j + 1)
            .asSequence()
            .filter { (x, y) ->
                x >= 0 
                && x <= matrix.size - 1
                && y >= 0
                && y <= matrix[0].size - 1
            }.forEach { next ->
                val (x, y) = next
                if (next in visited) {
                    Unit
                } else if (matrix[x][y] == '0') {
                    bfs(matrix, next, table, visited)
                } else {
                    table.getOrPut(matrix[x][y]) { mutableSetOf<Pair<Int, Int>>() }.add(next)
                }
            }
    }
    
    fun solution(storage: Array<String>, requests: Array<String>): Int {
        val matrix = storage.map { it.toMutableList() }.toList()
        
        requests.forEach { request ->
            val target = request[0]
            when (request.length) {
                1 -> {
                    val table = mutableMapOf<Char, MutableSet<Pair<Int, Int>>>()
                    matrix.forEachIndexed { i, row ->
                        row.forEachIndexed { j, item -> 
                            if (i == 0 
                                || i == matrix.size - 1
                                || j == 0
                                || j == matrix[0].size - 1) {  
                                table.getOrPut(matrix[i][j]) { mutableSetOf<Pair<Int, Int>>() }.add(i to j)
                            } 
                        }
                    }
                    val visited = mutableSetOf<Pair<Int, Int>>()
                    table['0']?.forEach { empty ->
                        bfs(matrix, empty, table, visited)                        
                    }
                    
                    table[target]?.forEach { (x, y) ->
                        matrix[x][y] = '0'
                    }       
                } else -> {
                    val table = mutableMapOf<Char, MutableSet<Pair<Int, Int>>>()
                    
                    matrix.forEachIndexed { i, row ->
                        row.forEachIndexed { j, item -> 
                            if (matrix[i][j] != '0') {
                                table.getOrPut(matrix[i][j]) { mutableSetOf<Pair<Int, Int>>() }.add(i to j)
                            } 
                        }
                    }
                    
                    table[target]?.forEach { (x, y) ->
                        matrix[x][y] = '0'
                    }       
                }
            }
        }
        
        return matrix.sumOf { row -> row.count { it != '0' }}
    }
}

// O(r * n * m)
// 접근 가능한 컨테이너: 테두리에 있는 컨테이너
// 테두리에 있는 빈 영역과 연결되는 컨테이너
// 요청 1: 매번 BFS를 돌려 접근 가능한 컨테이너, 테두리에 있는 빈 영역과 연결되는 컨테이너 리스트 만들고 여기서 해당하는 것 제거
// 요청 2: 컨테이너 전체 순환하면서 해당하는 것 제거