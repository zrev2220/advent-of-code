import kotlin.time.TimeSource

val timeSource = TimeSource.Monotonic
val startTime = timeSource.markNow()

Runtime.getRuntime()
  .addShutdownHook(Thread { println("ran in ${timeSource.markNow() - startTime}") })

var ans = 0

while (true) {
  val line = readlnOrNull()?.trim() ?: break
  val parts = line.split(" ")
  val lights = parts[0]
  val buttons = parts.slice(1..<parts.size - 1)

  val goal =
    lights.slice(1..<lights.length - 1).foldIndexed(0) { i, acc, c ->
      when (c) {
        '.' -> acc
        '#' -> acc or (1 shl i)
        else -> error("Unexpected character: $c")
      }
    }

  val operations =
    buttons.map {
      it
        .slice(1..<it.length - 1)
        .split(",")
        .map { it.toInt() }
        .fold(0) { acc, button -> acc or (1 shl button) }
    }

  val distance = mutableMapOf(0 to 0)
  val queue = mutableListOf(0)
  while (queue.size != 0) {
    val state = queue.removeFirst()
    val stateDistance = distance[state] ?: error("State ${state.toString(2)} has null distance")

    if (state == goal) {
      ans += stateDistance
      break
    }

    for (op in operations) {
      val nextState = state xor op
      if (nextState in distance) continue
      queue.add(nextState)
      distance[nextState] = stateDistance + 1
    }
  }
}

println(ans)
