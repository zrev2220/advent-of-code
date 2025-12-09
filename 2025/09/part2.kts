import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min
import kotlin.time.TimeSource

val timeSource = TimeSource.Monotonic
val startTime = timeSource.markNow()

Runtime.getRuntime()
  .addShutdownHook(Thread { println("ran in ${timeSource.markNow() - startTime}") })

typealias Point = Pair<Int, Int>

val points = mutableListOf<Point>()

while (true) {
  val coords = readlnOrNull()?.trim()?.split(',')?.map { it.toInt() } ?: break

  points.add(coords[0] to coords[1])
}

val N = points.size

fun isPointOnEdge(p: Point, _a: Point, _b: Point): Boolean {
  // sort points by x, then y
  val (a, b) = listOf(_a, _b).sortedWith(compareBy({ it.first }, { it.second }))
  return (a.second == p.second &&
    b.second == p.second &&
    a.first <= p.first &&
    p.first <= b.first) ||
    (a.first == p.first && b.first == p.first && a.second <= p.second && p.second <= b.second)
}

fun inPolygon(p: Point): Boolean {
  // https://www.geeksforgeeks.org/cpp/point-in-polygon-in-cpp/#c-program-to-check-point-in-polygon-using-raycasting-algorithm
  var intersections = 0
  for (i in 0..<N) {
    val a = points[i]
    val b = points[(i + 1) % N]

    if (isPointOnEdge(p, a, b)) return true

    if (
      (p.second > min(a.second, b.second)) &&
        (p.second <= max(a.second, b.second)) &&
        (p.first <= max(a.first, b.first))
    ) {
      val xIntersect = (p.second - a.second) * (b.first - a.first) / (b.second - a.second) + a.first
      if (a.first == b.first || p.first <= xIntersect) intersections++
    }
  }
  return intersections % 2 == 1
}

var best = 0
var bestRect: Pair<Point, Point>? = null

// from visually inspecting my input, consider only rectangles entirely above `aboveX`
// or entirely below `belowX`
// `null` if input is small, so running on example still works
var aboveX: Int? = null
var belowX: Int? = null

if (N > 100) {
  println("Large input size detected; using aboveX/belowX")
  println("==============================================")
  aboveX = 50402
  belowX = 48336
} else {
  println("Small input size detected, NOT using aboveX/belowX")
  println("==================================================")
}

var checked = 0
val total = (N * (N - 1)) / 2

for (i in 0..<N) {
  for (j in i + 1..<N) {
    val a = points[i]
    val b = points[j]
    val c = a.first to b.second
    val d = b.first to a.second

    // ensure rect fits in the polygon
    val rect = listOf(a, b, c, d)
    val newPoints = listOf(c, d)
    if (
      (aboveX == null ||
        belowX == null ||
        rect.all { it.second >= aboveX!! } ||
        rect.all { it.second <= belowX!! }) && newPoints.all { inPolygon(it) }
    ) {
      val area = (abs(a.first - b.first) + 1) * (abs(a.second - b.second) + 1)
      if (area > best) {
        best = area
        bestRect = a to b
      }
    }
  }
}

println()

println("Answer: $best")

println("for this rectangle: $bestRect")
