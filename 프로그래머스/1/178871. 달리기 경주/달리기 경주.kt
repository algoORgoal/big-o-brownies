// Array를 Map으로 변환
// callings를 순회하면서 Map에 있는 원소를 swap
// 시간복잡도: n + m


class BiMap<K, V>() {
    private val forward = mutableMapOf<K, V>()
    private val backward = mutableMapOf<V, K>()
    
    constructor(mappings: List<Pair<K, V>>): this() {
        mappings.forEach { (key, value) ->
            forward[key] = value
            backward[value] = key   
        }
    }
    
    fun get(key: K): V? = forward[key]
    
    fun getKey(value: V): K? = backward[value]
    
    fun put(key: K, value: V) {
        forward[key]?.let { oldValue ->
            if (backward[oldValue] != null) backward.remove(oldValue)
        }
        
        backward[value]?.let { oldKey ->
            if (forward[oldKey] != null) forward.remove(oldKey)
        }
        
        forward[key] = value
        backward[value] = key
    }
    
    fun pairs(): List<Pair<K, V>> {
        return forward.map { (k, v) -> k to v }
    }
}

class Solution {
    
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        val pairs = players.mapIndexed { index, player -> player to index }
        val playerRankingTable = BiMap<String, Int>(pairs)
        
        val afterRaceTable = callings.fold(playerRankingTable) { acc, player ->
            val currentRank = acc.get(player) ?: 0
            val aheadRank = currentRank - 1
            val aheadPlayer = acc.getKey(aheadRank) ?: ""
            acc.put(player, aheadRank)
            acc.put(aheadPlayer, currentRank)
            acc
        }
        
        return afterRaceTable.pairs().sortedBy() { (key, value) -> value }.map { (key, value) -> key }.toList().toTypedArray()
    }
}