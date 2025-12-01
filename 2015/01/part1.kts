val input = readln().trim()

var floor = 0

for (char in input) {
  floor +=
    when (char) {
      '(' -> 1
      ')' -> -1
      else -> 0
    }
}

println(floor)
