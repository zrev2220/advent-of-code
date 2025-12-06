import kotlin.math.max
import kotlin.math.pow

val grid = mutableListOf<String>()
var W = 0
var H = 0

while (true) {
  val line = readlnOrNull() ?: break
  W = max(W, line.length)
  H++
  grid.add(line)
}

grid.forEachIndexed { i, line ->
  if (line.length < W) {
    grid[i] = line.padEnd(W, ' ')
  }
}

val operators = grid[H - 1].split(Regex(" +"))

fun solve(col: Int, problemIndex: Int): Long {
  val h = H - 1
  val operator = operators[problemIndex]
  var ans =
    when (operator) {
      "*" -> 1L
      "+" -> 0L
      else -> error("Unsupported operator: $operator")
    }
  for (j in col downTo 0) {
    if (grid.all { it[j] == ' ' }) break
    var operand = 0L
    for (i in 0..<h) {
      if (grid[i][j] == ' ') operand /= 10
      else operand += (grid[i][j].digitToInt().toDouble() * (10.0).pow(h - i - 1)).toLong()
    }
    when (operator) {
      "*" -> ans *= operand
      "+" -> ans += operand
      else -> error("Unsupported operator: $operator")
    }
  }
  return ans
}

var ans = 0L
var problemIndex = 0

for (col in 0..<W) {
  if (col + 1 == W) {
    ans += solve(col, problemIndex++)
  } else if (grid.all { it[col] == ' ' }) {
    ans += solve(col - 1, problemIndex++)
  }
}

println(ans)
