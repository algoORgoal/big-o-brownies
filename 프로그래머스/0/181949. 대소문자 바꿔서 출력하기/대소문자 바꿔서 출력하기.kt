fun main(args: Array<String>) {
    val str = readLine()!!
    val strArray = str.map {
        when(it) {
            in 'a'..'z' -> (it.code - 32).toChar()
            in 'A'..'Z' -> (it.code + 32).toChar()
            else -> it
        }
    }
    println(strArray.joinToString(""))
}