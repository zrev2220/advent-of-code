import kotlin.math.max
import kotlin.system.exitProcess

var ans = 0

while (true) {
  val line = readlnOrNull()?.trim() ?: break

  var best: Int? = null
  var highest: Int? = null
  for (c in line) {
    val cint = c.digitToInt()
    if (highest == null) {
      highest = cint
      continue
    }

    val current = "$highest$c".toInt()
    best = if (best == null) current else max(best, current)

    highest = max(highest, cint)
  }

  if (best != null) {
    ans += best
  } else {
    System.err.println("`best` not defined after loop!")
    exitProcess(1)
  }
}

println(ans)
