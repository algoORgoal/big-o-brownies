class Solution {
    fun solution(s: String): String {
        if (s.all { it == ' ' }) return s
        return s.trim()
            .split("[ ]+".toRegex())
            .map {
                when (it[0]) {
                    in 'a'..'z' -> it[0].uppercase() + it.slice(1 until it.length).lowercase()
                    else -> it[0] + it.slice(1 until it.length).lowercase()
                } 
            }.let {                
                val spaces = s.split("[0-9a-zA-Z]+".toRegex()).filter { it != "" }
                when {
                    s.startsWith(" ") && s.endsWith(" ") -> spaces.foldIndexed("") { index, acc, element ->
                        acc + when (index) {
                            spaces.size - 1 -> element
                            else -> element + it[index]
                        }
                    }
                    s.startsWith(" ") -> spaces.foldIndexed("") { index, acc, element ->
                        acc + element + it[index]
                    }
                    
                    s.endsWith(" ") -> spaces.foldIndexed("") { index, acc, element ->
                        acc + it[index] + element
                    }
                    
                    else -> spaces.foldIndexed("") { index, acc, element ->
                        acc + it[index] + element
                    } + it[it.size - 1]
                }
            }
            
    }
}