Hints:

- Day 10, part 2:
  - Perused r/adventofcode for ideas on how to approach the problem:
    - [Link](https://www.reddit.com/r/adventofcode/comments/1pj68n4/2025_day_10_me_opening_this_sub/) - People are using Z3 for this (I had never used it before).
    - [Link](https://www.reddit.com/r/adventofcode/comments/1pjkj0h/2025_day_10_part_2_simplex_method_anyone/) - Simplex / Linear Programming may work.
      - I had not heard of this until coincidentally reading about it in _Competitive Programming 4_ that same day. I did not end up using this, though.
    - [Link](https://www.reddit.com/r/adventofcode/comments/1pjghln/2025_day_10_part_2_is_the_problem_possible_to/) - Idea to solve matrix, then brute force free variables.
  - Used AI coding tools for the following:
    - How to use `z3-solver` in Python (Z3's docs are pretty opaque).
    - How to use multiprocessing to parallelize brute forcing free variables portion of the solution.
