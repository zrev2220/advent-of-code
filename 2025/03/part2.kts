var ans = 0L
var MAX = 12

while (true) {
  val batteries = readlnOrNull()?.trim()?.map { c -> c.digitToInt() } ?: break

  fun pickHighest(start: Int, remaining: Int): Int {
    val end = batteries.size - remaining
    var bestIndex: Int? = null

    for (j in start..end) {
      if (bestIndex == null || batteries[j] > batteries[bestIndex]) bestIndex = j
    }

    checkNotNull(bestIndex) { "bestIndex is null" }
    return bestIndex
  }

  var start = 0
  var remaining = MAX
  val best = mutableListOf<Int>()
  while (remaining > 0) {
    val highestIndex = pickHighest(start, remaining--)
    best.add(batteries[highestIndex])
    start = highestIndex + 1
  }

  val bestNumber = best.joinToString("").toLong()
  ans += bestNumber
}

println(ans)
