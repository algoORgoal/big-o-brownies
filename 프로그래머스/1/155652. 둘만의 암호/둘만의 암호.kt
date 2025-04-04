class BiMap<K, V>() {
    private val forward = mutableMapOf<K, V>()
    private val backward = mutableMapOf<V, K>()
    
    constructor(pairs: List<Pair<K,V>>): this() {
        pairs.forEach { (key, value) ->
            forward[key] = value
            backward[value] = key
        }
    }
    
    fun get(key: K): V? = forward[key]
    fun getKey(value: V): K? = backward[value]
    
    fun size(): Int = forward.size
}


class Solution {
    fun solution(s: String, skip: String, index: Int): String {
        
        val pairs = ('a'..'z').fold(emptyList<Pair<Char, Int>>()) { acc, char -> 
            when {
                !(char in skip) -> acc + (char to acc.size)
                else -> acc
            }
        }
        val biMap = BiMap(pairs)
        
        val newS = s.map { char ->
            val order = biMap.get(char) ?: 0
            val newOrder = (order + index) % biMap.size()
            biMap.getKey(newOrder) ?: 'a'
        }.joinToString("")
        return newS
    }
}