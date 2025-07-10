import kotlin.math.pow
import kotlin.math.max

class Solution {
    fun solution(info: Array<IntArray>, n: Int, m: Int): Int {
        var dp = (0..n).map {
            (0..m).map { 0 }.toMutableList()
        }.toMutableList<MutableList<Int>>()
        
        info.map { it[0] to it[1] }.forEach { (a, b) ->
            val temp1 = (0..n).map {
                (0..m).map { 0 }.toMutableList()
            }.toMutableList<MutableList<Int>>()
            
            val temp2 = (0..n).map {
                (0..m).map { 0 }.toMutableList()
            }.toMutableList<MutableList<Int>>()

            for (i in 0..n) {
                for (j in 0..m) {
                    if (dp[i][j] >= 1 || (i == 0 && j == 0)) {
                        if (i + a <= n) {
                            temp1[i + a][j] = max(dp[i + a][j], dp[i][j] + 1)
                        }
                        if (j + b <= m) {
                            temp2[i][j + b] = max(dp[i][j + b], dp[i][j] + 1)
                        }      
                    }  
                }   
            }
            
            for (i in 0..n) {
                for (j in 0..m) {
                    dp[i][j] = listOf(temp1[i][j], temp2[i][j], dp[i][j]).maxOrNull() ?: 0
                }
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