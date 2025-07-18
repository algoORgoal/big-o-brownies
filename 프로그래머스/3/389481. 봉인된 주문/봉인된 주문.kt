import kotlin.math.pow

class Solution {
    fun sum(string: String): Long {
        val sum = string.reversed().withIndex().sumOf { (index, char) ->
            (char - 'a' + 1) * 26.toDouble().pow(index)
        }
        return sum.toLong()
    }
    
    fun generate(number: Long): String {
        val queue = ArrayDeque<Long>()
        
        var current = number
        while (current > 0) {
            val temp = current - 1
            val remainder = temp % 26
            queue.addFirst(remainder)
            
            val quotient = temp / 26
            current = quotient
        }
        
        return queue.fold("") { acc, number ->
            acc + ('a' + number.toInt()).toChar()
        }
    }
    
    fun solution(n: Long, bans: Array<String>): String {
        val sortedBans = bans.sortedWith(Comparator<String> { a, b -> 
            when (a.length != b.length) {
                true -> a.length - b.length
                else -> sum(a).compareTo(sum(b))
            }
        })
        
        val number = sortedBans.fold(n) { acc, ban ->
            val sum = ban.reversed().withIndex().sumOf { (index, char) ->
                (char - 'a' + 1) * 26.toDouble().pow(index)
            }
            if (acc >= sum) {
                acc + 1
            } else {
                acc
            }
        }
        
        return generate(number)
    }
}

// 10진수로 변환
// ban 요소가 n보다 작을 때마다 n을 1만큼 증가 => k번째 요소를 지웠을 때, 본래 문자의 인덱스가 모두 한칸씩 이동하는 꼴

// a = 1
// z = 26
// aa = 1 * 26^1 + 1 * 26^0 = 27
// az = 1 * 26^1 + 26 * 26^0 = 52
// ba = 2 * 26^1 + 1 * 26^0 = 53
// bz = 2 * 26^1 + 26 * 26^0 = 52 + 26 = 78
// zz = 26 * 26^1 + 26 * 26^0
// aaa = 1 * 26^2 + 1 * 26^1 + 1 * 26^0

// a => 0
// z => 25
// aa -> 1 * 25^1 + 1 * 25^0 = 26
// az -> 1 * 25^1 + 25 * 25^0 = 50
// zz -> 25 * 25^1 + 25 * 25^0
// aaa -> 

// aa => 27
// 1 * 26^1 + 0 * 26^1 = 26
// az => 1 * 26^1 + 25 * 26^0 = 51
// ba => 2 * 26^1 + 0 * 26^0 = 52
// bb => 2 * 26^1 + 1 * 26^0 = 52
// bz => 2 * 26^1 + 25 * 26^0 = 52 + 25 = 75
// zz => 26 * 26^1 + 25 * 26^0 = 26 ^ 2 + 25 ^ 26 ^ 1 =


// ae = 1 * 26^1 + 5 * 26^0 = 31
// ah = 1 * 26^1 + 8 * 26^0 = 26 + 8 = 34
// aa = 1 * 26^1 + 1 * 26^0 = 27

//  2 32
//.   16 --- 0
//.   8 --- 0
//.   4 ---- 0
//      2 ---- 0
//      1


// 9
// 4 --- 1
// 2 --- 0
// 1 --- 0
// aaz = 1 * 26^2 + 1 * 26^1 + 26 * ^0
// 그냥 10(26) => z
// 11 => az