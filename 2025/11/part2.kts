val adjList = mutableMapOf<String, List<String>>()

while (true) {
  val line = readlnOrNull()?.trim() ?: break
  val (node, others) = line.split(": ")
  adjList[node] = others.split(" ")
}

val overallStart = "svr"
val overallEnd = "out"
val keyNodes = listOf("dac", "fft")

val banSet = mutableSetOf<String>()
val tempBan = mutableSetOf<String>()

fun dfs(node: String, end: String): Int {
  val neighbors = adjList[node] ?: error("Node $node not in adjList")
  var ans = 0
  for (neighbor in neighbors) {
    if (neighbor in banSet) continue
    tempBan.add(neighbor)
    if (neighbor == end) {
      ans++
    } else {
      ans += dfs(neighbor, end)
    }
  }
  return ans
}

var ans = 1L
val itenerary = listOf(overallEnd) + keyNodes + listOf(overallStart)

for (i in 1..<itenerary.size) {
  val value = dfs(node = itenerary[i], end = itenerary[i - 1])
  ans *= value
  banSet.addAll(tempBan)
  tempBan.clear()
}

println(ans)
