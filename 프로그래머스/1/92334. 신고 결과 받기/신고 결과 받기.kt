class Solution {
    fun solution(idList: Array<String>, report: Array<String>, k: Int): IntArray {
        val graph = idList.fold(mutableMapOf<String, Pair<MutableSet<String>, MutableSet<String>>>()) { acc, id ->
            acc[id] = mutableSetOf<String>() to mutableSetOf<String>()
            acc
        }
        val reportedGraph = report.fold(graph) { acc, str ->
            val (reporter, reported) = str.split(" ")
            acc[reporter]?.let { it.first.add(reported) }
            acc[reported]?.let { it.second.add(reporter) }
            acc
        }
        return reportedGraph.toList().map { (person, pair) ->
            val reportingList = pair.first
            reportingList.filter { reported -> (reportedGraph[reported]?.let{ it.second.size } ?: 0) >= k }.size
        }.toIntArray()
    }
}