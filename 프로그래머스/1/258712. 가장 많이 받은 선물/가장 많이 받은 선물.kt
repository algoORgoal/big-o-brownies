// a가 b에게 선물을 준 횟수를 map으로 기록한다.
// a가 친구들에게 선물을 준/받은 횟수를 map 기록한다.
// 모든 친구들을 combination으로 만들고, 다음 달에 선물을 받는 사람을 기록한다.

class Solution {
    fun List<String>.combination(): List<Pair<String, String>> {
        return this.foldIndexed(emptyList<Pair<String, String>>()) { index, acc, first ->
            acc + this.drop(index + 1).map { second -> first to second }
        }
    }
    
    fun solution(friends: Array<String>, gifts: Array<String>): Int {
        val pairTable = gifts.map { 
            val (sender, taker) = it.split(' ')
            Pair(sender, taker)
        }
        .fold(emptyMap<Pair<String, String>, Int>()) {
            acc, pair ->
            acc + (pair to acc.getOrElse(pair) { 0 } + 1)
        }
        
        val senderTable = pairTable.entries.fold(emptyMap<String, Int>()) {
            acc, (pair, count) ->
            val (sender, taker) = pair
            acc + (sender to acc.getOrElse(sender) { 0 } + count)
        }
        
        val takerTable = pairTable.entries.fold(emptyMap<String, Int>()) {
            acc, (pair, count) ->
            val (sender, taker) = pair
            acc + (taker to acc.getOrElse(taker) { 0 } + count)
        }
        
        val nextMonthTakerTable = friends.toList().combination().fold(emptyMap<String, Int>()) { acc, (first, second) -> 
            val firstCount = pairTable.getOrElse(Pair(first, second)) { 0 }
            val secondCount = pairTable.getOrElse(Pair(second, first)) { 0 }
            
            if (firstCount > secondCount) acc + (first to acc.getOrElse(first) { 0 } + 1)
            else if (firstCount < secondCount) acc + (second to acc.getOrElse(second) { 0 } + 1)
            else {
                val firstMetric = senderTable.getOrElse(first) { 0 } - takerTable.getOrElse(first) { 0 }
                val secondMetric = senderTable.getOrElse(second) { 0 } - takerTable.getOrElse(second) { 0 }
                if (firstMetric > secondMetric) acc + (first to acc.getOrElse(first) { 0 } + 1)
                else if (firstMetric < secondMetric) acc + (second to acc.getOrElse(second) { 0 } + 1)
                else acc
            }
        }
        
        return nextMonthTakerTable.values.toList().maxOrNull() ?: 0
    }
}