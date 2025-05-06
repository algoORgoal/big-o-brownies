fun main(args: Array<String>) {
    val (a, b) = readLine()!!.split(' ').map(String::toInt)
    (0 until b).forEach {
        println(("*").repeat(a))
    }
}