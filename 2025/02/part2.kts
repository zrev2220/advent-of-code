fun checkPrefix(s: String, prefix: String): Boolean {
  val plen = prefix.length
  if (s.length % plen != 0) return false
  for (i in plen..s.length - plen step plen) {
    if (s.substring(i, i + plen) != prefix) return false
  }
  return true
}

val input = readln().trim()

var ans = 0L

val ranges = input.split(',')

for (range in ranges) {
  val bounds = range.split('-')
  val min = bounds[0].toLong()
  val max = bounds[1].toLong()

  for (i in min..max) {
    val s = i.toString()

    for (j in 1..s.length / 2) {
      val prefix = s.substring(0, j)
      if (checkPrefix(s, prefix)) {
        ans += i
        break
      }
    }
  }
}

println(ans)
