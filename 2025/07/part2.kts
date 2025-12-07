val grid = mutableListOf<String>()
var W = 0
var H = 0
var start = -1

while (true) {
  val line = readlnOrNull()?.trim() ?: break
  grid.add(line)
  W = line.length
  H++
  val possibleStart = line.indexOf('S')
  if (possibleStart >= 0) start = possibleStart
}

val memo = mutableMapOf<Pair<Int, Int>, Long>()

fun traverse(pos: Pair<Int, Int>): Long {
  memo[pos]?.let {
    return it
  }

  val next = pos.first + 1 to pos.second
  val result =
    when {
      next.first !in 0..<W || next.second !in 0..<H -> 0
      grid[next.first][next.second] == '^' -> {
        listOf(next.first to next.second - 1, next.first to next.second + 1)
          .map { if (it.first in 0..<W && it.second in 0..<H) traverse(it) else 0 }
          .sum() + 1L
      }

      grid[next.first][next.second] == '.' -> traverse(next)
      else -> error("`else` should not happen")
    }
  memo[pos] = result
  return result
}

println(traverse(0 to start) + 1)
