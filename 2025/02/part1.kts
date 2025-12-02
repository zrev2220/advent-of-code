val input = readln().trim()

var ans = 0L

val ranges = input.split(',')

for (range in ranges) {
  val bounds = range.split('-')
  val min = bounds[0].toLong()
  val max = bounds[1].toLong()

  for (i in min..max) {
    val s = i.toString()
    if (s.length % 2 != 0) continue
    val firstHalf = s.subSequence(0, s.length / 2).toString()
    val lastHalf = s.subSequence(s.length / 2, s.length).toString()
    if (firstHalf == lastHalf) ans += i
  }
}

println(ans)
