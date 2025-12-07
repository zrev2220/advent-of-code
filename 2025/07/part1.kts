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

val queue = mutableListOf(0 to start)
val visited = mutableSetOf<Pair<Int, Int>>()

var ans = 0

while (queue.size > 0) {
  val pos = queue.removeFirst()
  if (visited.contains(pos)) continue
  visited.add(pos)
  val next = pos.first + 1 to pos.second
  when {
    next.first !in 0..<W || next.second !in 0..<H -> continue
    grid[next.first][next.second] == '^' -> {
      ans++
      listOf(next.first to next.second - 1, next.first to next.second + 1).forEach {
        if (it.first in 0..<W && it.second in 0..<H) queue.add(it)
      }
    }

    grid[next.first][next.second] == '.' -> queue.add(next)
    else -> error("`else` should not happen")
  }
}

println(ans)
