var dial = 50
var pw = 0
val size = 100

fun rotate(current: Int, dist: Int) = Math.floorMod(current + dist, size)

var _line = readlnOrNull()

while (_line != null) {
  val line = _line!!
  val left = line[0] == 'L'
  val rawDist = line.subSequence(1, line.length).toString().toInt()
  val dist = rawDist * (if (left) -1 else 1)

  val old = dial
  dial = rotate(dial, dist)

  val toFirstClick = if (left) old else size - old
  val clicks =
    (if (rawDist >= toFirstClick && toFirstClick != 0) 1 else 0) + ((rawDist - toFirstClick) / size)
  pw += clicks

  _line = readlnOrNull()
}

println(pw)
