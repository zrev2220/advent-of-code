val adjList = mutableMapOf<String, MutableList<String>>()

while (true) {
  val line = readlnOrNull()?.trim() ?: break
  val (node, others) = line.split(": ")
  for (other in others.split(" ")) {
    val neighbors = adjList.getOrPut(node) { mutableListOf() }
    neighbors.add(other)
  }
}

val start = "you"
val end = "out"

fun dfs(node: String): Int {
  val neighbors = adjList[node] ?: error("Node $node not in adjList")
  var ans = 0
  for (neighbor in neighbors) {
    if (neighbor == end) ans++ else ans += dfs(neighbor)
  }
  return ans
}

println(dfs(start))
