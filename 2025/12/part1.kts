val shapes = mutableListOf<MutableList<String>>()
val shapeTiles = mutableListOf<Int>()

for (i in 0..5) {
  readln()
  val shape = mutableListOf<String>()
  var tiles = 0
  for (j in 1..3) {
    val line = readln().trim()
    shape.add(line)
    tiles += line.count { it == '#' }
  }
  shapes.add(shape)
  shapeTiles.add(tiles)

  readln()
}

var yes = 0
var no = 0
var maybe = 0

while (true) {
  val line = readlnOrNull()?.trim() ?: break
  val regex = """(?<width>\d+)x(?<height>\d+):(?<quantities>(?: \d+){6})""".toRegex()
  val match = regex.matchEntire(line) ?: error("Line '$line' did not match regex")
  val width = match.groups["width"]!!.value.toInt()
  val height = match.groups["height"]!!.value.toInt()
  val quantities = match.groups["quantities"]!!.value.trim().split(" ").map { it.toInt() }

  val space = width * height
  val payloadMin = quantities.mapIndexed { i, q -> shapeTiles[i] * q }.sum()

  val spaceNaive = (width / 3) * (height / 3)
  val payloadNaive = quantities.sum()

  when {
    payloadNaive <= spaceNaive -> yes++
    payloadMin > space -> no++
    else -> maybe++
  }
}

println("yes:   $yes")

println("no:    $no")

println("maybe: $maybe")
