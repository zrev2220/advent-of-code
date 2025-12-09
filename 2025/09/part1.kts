import kotlin.math.abs
import kotlin.math.max

val tiles = mutableListOf<Pair<Int, Int>>()

while (true) {
  val coords = readlnOrNull()?.trim()?.split(',')?.map { it.toInt() } ?: break

  tiles.add(coords[1] to coords[0])
}

val sortedTiles = tiles.sortedWith(compareBy({ it.first }, { it.second }))

var best = 0L

for (i in sortedTiles.indices) {
  for (j in i + 1..<sortedTiles.size) {
    val a = tiles[i]
    val b = tiles[j]
    val area = abs(a.first - b.first + 1).toLong() * abs(a.second - b.second + 1).toLong()
    best = max(best, area)
  }
}

println(best)
