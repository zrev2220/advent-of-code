val endpoints = mutableListOf<Pair<Long, Boolean>>()

while (true) {
  val line = readln().trim()
  if (line == "") break
  val range = line.split('-').map { it.toLong() }
  endpoints.addAll(listOf(range[0] to true, range[1] to false))
}

var _currentStart: Long? = null
var openRanges = 0L
var ans = 0L

for ((endpoint, isOpening) in endpoints.sortedWith(compareBy({ it.first }, { !it.second }))) {
  val currentStart = _currentStart
  if (currentStart == null) {
    _currentStart = endpoint
    openRanges++
    continue
  }

  if (isOpening) openRanges++
  else {
    openRanges--
    if (openRanges == 0L) {
      ans += endpoint - currentStart + 1
      _currentStart = null
    }
  }
}

println(ans)
