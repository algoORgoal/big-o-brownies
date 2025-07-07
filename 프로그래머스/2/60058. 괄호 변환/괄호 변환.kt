class Solution {
    fun isCorrect(w: String): Boolean {
        val stack = ArrayDeque<Char>();
        w.forEach {
            when (it) {
                '(' -> {
                    stack.addLast(it)
                }
                ')' -> {
                    if (stack.isEmpty()) return false
                    stack.removeLast()
                }
            }
        }
        return true
    }
    
    // ((()))()
    // ((()))와 ()를 구분할 수 있어야 함
    
    fun splitBalancedSubstrings(w: String): Pair<String, String> {
        var count = if (w[0] == '(') 1 else -1

        for (i in 1 until w.length) {
            when (w[i]) {
                '(' -> count += 1
                else -> count -= 1
            }
            if (count == 0) {
                return w.slice(0..i) to w.slice(i + 1 until w.length)
            }
        }
        
        return "" to ""
    }
    
    fun solution(w: String): String {
        if (isCorrect(w)) return w
        val (u, v) = splitBalancedSubstrings(w)
        if (isCorrect(u)) return u + solution(v)
        return '(' + solution(v)  + ')' + u.slice(1 until u.length - 1)
            .map { if (it == '(') ')' else '('}.joinToString("")
        
    }
}