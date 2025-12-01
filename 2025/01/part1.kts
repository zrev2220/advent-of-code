var dial = 50
var pw = 0
val size = 100

fun rotate(current: Int, left: Boolean, dist: Int) =
  (size + (current + ((dist) * (if (left) -1 else 1)))) % size

var _line = readlnOrNull()

while (_line != null) {
  val line = _line!!
  val left = line[0] == 'L'
  val dist = line.subSequence(1, line.length).toString().toInt()

  dial = rotate(dial, left, dist)
  if (dial == 0) pw++

  _line = readlnOrNull()
}

println(pw)
