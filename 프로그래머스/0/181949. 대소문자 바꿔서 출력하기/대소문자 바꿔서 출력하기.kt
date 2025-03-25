fun main(args: Array<String>) {
    val str = readLine()!!
    val strArray = str.map {
        when(it) {
            in 'a'..'z' -> (it.code - ('a' - 'A')).toChar()
            in 'A'..'Z' -> (it.code + ('a' - 'A')).toChar()
            else -> it
        }
    }
    println(strArray.joinToString(""))
}