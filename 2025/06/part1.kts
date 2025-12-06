val problems = mutableListOf<MutableList<Long>>()

while (true) {
  val line = readln().trim().split(Regex(" +"))
  try {
    line.forEachIndexed { i, s ->
      if (problems.size <= i) problems.add(mutableListOf(s.toLong()))
      else problems[i].add(s.toLong())
    }
  } catch (e: NumberFormatException) {
    var ans = 0L
    line.forEachIndexed { i, operator ->
      ans +=
        when (operator) {
          "*" -> problems[i].fold(1L) { acc, n -> acc * n }
          "+" -> problems[i].sum()
          else -> error("Unsupported operator: $operator")
        }
    }
    println(ans)
    break
  }
}
