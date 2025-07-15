class Solution {
    fun solution(info: Array<String>, queries: Array<String>): IntArray {
        val scoreTable = info.flatMap { 
            val tokens = it.split(" ")
            val options = tokens.slice(0 until tokens.size - 1)
            val score = tokens.last().toInt()
            
            val pairs = (0..15).map { mask ->
                val key = options.mapIndexed { index, option ->
                    when (mask and (1 shl index)) {
                        0 -> '-'
                        else -> option
                    }
                }.joinToString(" ")
                key to score
            }
            pairs
        }.fold(mutableMapOf<String, MutableList<Int>>()) { acc, (key, score) ->
            if (!(key in acc)) {
                acc[key] = mutableListOf<Int>()
            }
            acc[key]!!.add(score)
            acc
        }
        scoreTable.values.map { mutableList ->
            mutableList.sort()
        }
        
        
        
        val result = queries.asSequence().map { query ->
            val tokens = query.split(" ").filter { it != "and" }
            val options = tokens.slice(0 until tokens.size - 1)
            val key = options.joinToString(" ")
            val score = tokens.last().toInt()
            
            val list = scoreTable[key] ?: emptyList<Int>()
            val count = if (list.isEmpty() || score > list.last()) {
                0
            } else {
                var start = 0
                var end = list.size - 1


                while (start < end) {
                    val middle = (start + end) / 2
                    // lowerbound = min(i | list[i] >= score)
                    if (score <= list[middle]) { // lowerbound <= list[middle]
                        end = middle
                    } else { // list[middle] < score, max(j | list[j] < score) < min(i | list[i] >= score) = lowerbound
                        start = middle + 1
                    }
                }
                val lowerbound = end
                list.size - lowerbound      
            }
            count
        }.toList()
        
        return result.toIntArray()
    }
}


// len(info) = nlen(query) = m
// mapping table에 담음 O(n), n <= 50_000
// 각 query별로 이진탐색해서 계산 => O(mlogn) * 24 