class Solution {
    fun solution(playerCountList: IntArray, m: Int, k: Int): Int {
        var currentRunnerCount = 0
        var totalRunnerCount = 0
        var expirationTable = mutableMapOf<Int, Int>()
        
        playerCountList.forEachIndexed { time, playerCount ->
            if ((expirationTable[time] ?: 0) > 0) {
                currentRunnerCount -= (expirationTable[time] ?: 0)
                expirationTable[time] = 0
            }
            if (currentRunnerCount * (m + 1) <= playerCount) {
                val requiredRunnerCount = playerCount / m
                val issuedRunnerCount = requiredRunnerCount - currentRunnerCount
                currentRunnerCount += issuedRunnerCount
                totalRunnerCount += issuedRunnerCount
                expirationTable[time + k] = (expirationTable[time + k] ?: 0) + issuedRunnerCount
            }
        }
        
        return totalRunnerCount
    }
}

// 현재 증설된 서버의 수
// 증설 횟수
// 각 증설된 서버의 유효기간

// 각 시간 별로 (0 ~ 23)
// 1. 서버를 증설해야 하는지 확인
//    증설해야 한다면, 유효기간 넣고 현재 증설된 서버의 수 및 증설 횟수 추가
// 2. 삭제해야 하는 서버가 있는지 확인, 삭제하면 현재 증설된 서버의 수 감소
