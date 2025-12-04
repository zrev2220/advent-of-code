val grid = mutableListOf<String>()

var W = 0

while (true) readlnOrNull()?.trim()?.let {
  grid.add(it)
  W = it.length
} ?: break

val H = grid.size

var ans = 0

for (i in 0..<H) for (j in 0..<W) {
  if (grid[i][j] != '@') continue

  var surrounding = 0
  val dirs = listOf(1 to -1, 1 to 0, 1 to 1, 0 to -1, 0 to 1, -1 to -1, -1 to 0, -1 to 1)
  for ((di, dj) in dirs) {
    val i2 = i + di
    val j2 = j + dj
    if (grid.elementAtOrNull(i2)?.elementAtOrNull(j2) == '@') surrounding++
  }

  if (surrounding < 4) ans++
}

println(ans)
