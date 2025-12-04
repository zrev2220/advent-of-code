val grid = mutableListOf<String>()

var W = 0

while (true) readlnOrNull()?.trim()?.let {
  grid.add(it)
  W = it.length
} ?: break

val H = grid.size

var ans = 0

data class Result(val grid: List<String>, val removed: Int)

fun remove(grid: List<String>): Result {
  var removed = 0
  val newGrid = mutableListOf<String>()
  for (i in 0..<H) {
    newGrid.add(
      buildString {
        for (j in 0..<W) {
          if (grid[i][j] != '@') {
            append(grid[i][j])
            continue
          }

          var surrounding = 0
          val dirs = listOf(1 to -1, 1 to 0, 1 to 1, 0 to -1, 0 to 1, -1 to -1, -1 to 0, -1 to 1)
          for ((di, dj) in dirs) {
            val i2 = i + di
            val j2 = j + dj
            if (grid.elementAtOrNull(i2)?.elementAtOrNull(j2) == '@') surrounding++
          }

          if (surrounding < 4) {
            removed++
            append('.')
          } else append(grid[i][j])
        }
      }
    )
  }
  return Result(newGrid, removed)
}

var currentGrid: List<String> = grid

while (true) {
  val result = remove(currentGrid)
  if (result.removed == 0) break
  ans += result.removed
  currentGrid = result.grid
}

println(ans)
