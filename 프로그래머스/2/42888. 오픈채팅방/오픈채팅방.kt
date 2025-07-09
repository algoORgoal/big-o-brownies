class Solution {
    fun solution(records: Array<String>): Array<String> {
        
        val publicHistory = records.map { record ->
            val key = record.split(' ')[1]
            val value = record.split(' ').let { if (it.size >= 3) listOf(it[0], it[2]) else listOf(it[0]) } 
            (key to value)
        }
        
        val historyTable = publicHistory.fold(mutableMapOf<String, MutableList<List<String>>>()) { acc, (uid, operation) ->
            if (uid in acc) {
                acc[uid]?.add(operation)
            } else {
                acc[uid] = mutableListOf<List<String>>(operation)    
            }
            acc
        }
        
        val nameTable = historyTable.entries.fold(mutableMapOf<String, String>()) { acc, (uid, activity) ->
            val stack = ArrayDeque(activity)
            while (stack.isNotEmpty()) {
                val current = stack.removeLast()                
                if (current[0] == "Change" || current[0] == "Enter") {
                    acc[uid] = current[1]
                    break
                } 
            }
            acc
        }
        
        
        return publicHistory.map { (uid, operation) ->
            when (operation[0]) {
                "Enter" -> nameTable[uid] + "님이 들어왔습니다."
                "Leave" -> nameTable[uid] + "님이 나갔습니다."
                else -> ""
            }
        }.filter { it.isNotEmpty() }.toTypedArray()
        
        // val historyList = historyTable.entries.map { (uid, activity) -> {
        //     activity.map { 
        //         when (it[0]) {
        //             "Enter" -> nameTable[uid] + "님이 들어왔습니다."
        //             "Leave" -> nameTable[uid] + "님이 나갔습니다."
        //             else -> {}
        //         }
        //     }
        // }
        
        return listOf("hi").toTypedArray()
    }
}


// 가장 마지막 히스토리가 [leave, enter] -> 
// 가장 마지막 히스토리가 [change] -> 해당 닉네임으로 표시
// Map을 통해 각 유저의 history를 표시
// 가장 마지막으로 leave,enter하거나 change한 부분 포착 => 닉네임 선정
