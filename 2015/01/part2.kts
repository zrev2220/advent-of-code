import kotlin.system.exitProcess

val input = readln().trim()

var floor = 0

for (i in input.indices) {
  val char = input[i]
  floor +=
    when (char) {
      '(' -> 1
      ')' -> -1
      else -> 0
    }
  if (floor < 0) {
    println(i + 1)
    exitProcess(0)
  }
}

System.err.println("Never entered the basement!")

exitProcess(1)
