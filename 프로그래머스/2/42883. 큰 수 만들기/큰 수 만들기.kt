

class Solution {
    fun solution(number: String, k: Int): String {
        val dq = arrayListOf<Char>()
        var removalCount: Int = 0
        number.forEach {
            var current: Char? = dq.lastOrNull()
            while (current != null && current.toInt() < it.toInt() && removalCount < k) {
                dq.removeAt(dq.size - 1)
                current = dq.lastOrNull()
                removalCount += 1
            }
            dq.add(it)
            
        }
        
        while (removalCount < k) {
            dq.removeAt(dq.size - 1)
            removalCount += 1
        }
        return dq.joinToString("")
    }
}

// 각 digit에 대하여
// stack top이 비어 있다 => 넣는다
// top < element => top >= element가 되거나, removeCount == k가 될 때까지 뺀다
// 여전히 removeCount < k => 맨 뒤쪽 빼버린다

// 19 24
// 924
// 94

// 1231234
// 231234
// 31234
// 3234

// 4177252841
// 4 => 4177252841 0
// 1 => 4177252841 1
// 7 => 4177252841 1
// 7 => 4177252841 1
// 2 => 417752841 2
// 5 => 417752841 2
// 2 => 41775841 2
// 77841
// 7841
// 841
//