val ranges = mutableListOf<Pair<Long, Long>>()

while (true) {
  val line = readln().trim()
  if (line == "") break
  val range = line.split('-').map { it.toLong() }
  ranges.add(range[0] to range[1])
}

var ans = 0

while (true) {
  val query = readlnOrNull()?.trim()?.toLong() ?: break

  if (ranges.any { it.first <= query && query <= it.second }) {
    ans++
  }
}

println(ans)
