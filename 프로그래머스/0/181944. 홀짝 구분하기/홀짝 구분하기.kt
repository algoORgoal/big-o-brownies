fun main(args: Array<String>) {
    val a = readLine()!!.toInt()
    val isEven = a % 2
    println("$a is ${if (a % 2 == 0) "even" else "odd"}")
}