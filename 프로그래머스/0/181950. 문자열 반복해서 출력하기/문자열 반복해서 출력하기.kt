fun main(args: Array<String>) {
    val (str, countStr) = readLine()!!.split(" ")
    val count = countStr.toInt()
    val repeatedStr = str.repeat(count)
    println("$repeatedStr")
}