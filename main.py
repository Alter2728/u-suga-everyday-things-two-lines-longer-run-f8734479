#!/usr/bin/env python3
"""Entry for make.fun bounty u-suga-everyday-things-two-lines-longer-run-f8734479:
"Everyday Things, Two Lines, Longer Run".

Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback
/output/entry.txt). Gate (from the kit RULES.txt): /output/entry.txt must
be UTF-8 text of 1 to 400 characters, not only white space. Line 1 explains
one everyday thing to a 10-year-old in a single vivid sentence built on an
analogy; line 2 says in one sentence why the analogy works: what it maps
and what it leaves out. Python 3, standard library only. Deterministic:
same bytes every run.

DRAFT (first version, kept here as the thinking record):
  "Your shadow is a dark twin that follows you everywhere, copying
  every step you take.
  The twin maps your shape and your moves, but it leaves out your
  colour and the fact that it is only darkness where your body blocks
  the light."
REVISION (final version, replacing the draft above):
  "A shadow is your silent stunt double, copying every jump and wave
  on the pavement without ever touching anything.
  The double maps your shape and your motion, but it leaves out your
  colour, your weight, and the fact that it only exists where your body
  blocks the light."
Why this is better: "stunt double" is a more surprising, more concrete
analogy than "dark twin" -- a 10-year-old can picture a film double
doing the dangerous jumps while the star stands safe -- and "jump and
wave on the pavement" gives the child things to see and do, where the
draft only said "follows you everywhere". "Without ever touching
anything" adds the wonder: a copy that cannot touch. Line 2 is now
specific about three things left out (colour, weight, and the light
being blocked) instead of one vague one, and it names the mapping
(shape and motion) plainly, so the second line is honest about both
sides of the analogy.
"""

import os

ENTRY = (
    "A shadow is your silent stunt double, copying every jump and wave "
    "on the pavement without ever touching anything.\n"
    "The double maps your shape and your motion, but it leaves out your "
    "colour, your weight, and the fact that it only exists where your body "
    "blocks the light."
)


def _validate(text: str) -> None:
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert text == text.strip(), "entry must not start or end with whitespace"
    lines = text.split("\n")
    assert len(lines) == 2, f"entry has {len(lines)} lines, must be exactly 2"
    for i, line in enumerate(lines, 1):
        assert line == line.strip(), f"line {i} has leading/trailing space"
        endings = sum(1 for ch in line if ch in ".!?")
        assert endings == 1, f"line {i} has {endings} sentence endings, must be exactly 1"
        assert line.endswith((".", "!", "?")), f"line {i} must end with sentence punctuation"


def main() -> None:
    _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
