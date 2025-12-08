import kotlin.math.pow
import kotlin.math.sqrt

val test = args.getOrElse(0) { "0" } != "0"

typealias Node = Triple<Int, Int, Int>

data class DisjointSet(val initialSize: Int) {
  val parent = MutableList(initialSize) { index -> index }
  val size = MutableList(initialSize) { 1 }

  fun find(n: Int): Int {
    if (parent[n] == n) return n
    parent[n] = find(parent[n])
    return parent[n]
  }

  fun union(a: Int, b: Int) {
    val aParent = find(a)
    val bParent = find(b)
    if (aParent == bParent) return
    parent[bParent] = aParent
    size[aParent] += size[bParent]
  }

  fun getAns(): Long {
    var remaining = 3
    var ans = 1L
    val sortedSizes =
      size.mapIndexed { index, value -> index to value }.sortedByDescending { it.second }
    for ((i) in sortedSizes) {
      if (remaining <= 0) break
      if (parent[i] != i) continue
      ans *= size[i]
      remaining--
    }
    return ans
  }
}

val nodes = mutableListOf<Node>()

while (true) {
  val line = readlnOrNull()?.split(",")?.map { it.toInt() } ?: break

  nodes.add(Triple(line[0], line[1], line[2]))
}

fun dist(a: Node, b: Node): Double =
  sqrt(
    (a.first - b.first).toDouble().pow(2) +
      (a.second - b.second).toDouble().pow(2) +
      (a.third - b.third).toDouble().pow(2)
  )

typealias Edge = Triple<Int, Int, Double>

val _edges = mutableListOf<Edge>()

for ((i, node) in nodes.withIndex()) {
  for (j in i + 1..<nodes.size) {
    val other = nodes[j]
    val d = dist(node, other)
    _edges.add(Triple(i, j, d))
  }
}

val edges = _edges.sortedBy { it.third }
val max = if (test) 10 else 1000

val dj = DisjointSet(nodes.size)

for (edge in edges.slice(0..<max)) {
  dj.union(edge.first, edge.second)
}

println(dj.getAns())
