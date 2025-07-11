import kotlin.math.pow
import kotlin.math.max

class Solution {
    fun solution(info: Array<IntArray>, n: Int, m: Int): Int {
        var dp = (0..n).map {
            (0..m).map { 0 }.toMutableList()
        }.toMutableList<MutableList<Int>>()
        
        info.map { it[0] to it[1] }.forEach { (a, b) ->
            val updates = mutableMapOf<Pair<Int, Int>, Int>()
            
            for (i in 0..n) {
                for (j in 0..m) {
                    if (dp[i][j] >= 1 || (i == 0 && j == 0)) {
                        if (i + a <= n) {
                            updates[i + a to j] = max(updates[i + a to j] ?: 0, dp[i][j] + 1)
                        }
                        if (j + b <= m) {
                            updates[i to j + b] = max(updates[i to j + b] ?: 0, dp[i][j] + 1)
                        }      
                    }  
                }   
            }
            
            updates.entries.map { (pair, value) -> 
                val (a, b) = pair
                dp[a][b] = max(dp[a][b], value)
            }
        }
        
        
        for (i in 0..n - 1) {
            for (j in 0..m - 1) {
                if (dp[i][j] == info.size) {
                    return i
                }
            }
        }
        
        return -1
    }

}


// f(a, b): A 도둑이 a개 흔적, b 도둑이 b개 흔적을 남길 때 훔친 물건의 인덱스 목록을 저장하면 되지 않나?
// f(a + info[i][0], b + info[i][1]) = f(a, b) 
// 단, 흔적은 도둑질을 할 수 있는 곳에만 남길 수 있다. f(a, b) >= 1 아니면 a = 0, b = 0이어야 함.