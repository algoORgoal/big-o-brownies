import kotlin.math.ceil
import kotlin.math.floor
import kotlin.math.abs

class Solution {
    fun getX(y: Int, w: Int, h: Int): Double {
        return - (y.toDouble() * w.toDouble() / h.toDouble())
    }
    
    
    fun solution(w: Int, h: Int): Long {
        val sum = (0 downTo (- (h - 1))).asSequence().fold(0.toLong()) { acc, y ->
            val x_1 = getX(y, w, h)
            val x_2 = getX(y - 1, w, h)
            
            val current = (ceil(x_1).toInt()..floor(x_2).toInt()).asSequence().count {
                it.toDouble() != x_1 && it.toDouble() != x_2
            } + 1
            
            acc + current.toLong()
        }
        return w.toLong() * h.toLong() - sum
    }
}

// y = ax + b
// a = (y1 - y2) / (x1 - x2)
// y = - (h / w) x
// x = - (w / h) y

// w = 8, h = 12 => y = - (3 / 2) x
// (2, -3)  => -3 = - (3 / 2) * 2 = -3

// k <= y_k <= k + 1 사이에 몇 개의 정수 x가 있는지 확인
// 0개 -> 1 정사각형 사용 불가
// 1개 -> 2 정사각형 사용 불가
// k개 -> k + 1 정사각형 사용 불가