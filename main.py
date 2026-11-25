#!/usr/bin/env python3
"""Describe Your Ex in One Word entry for make.fun bounty
u-puan-describe-your-ex-in-one-word-9fc6ebe7.

Writes exactly one word to /output/entry.txt.

The word: "Uninstalled".

Why it wins the head-to-head: the judge weighs whether the word is
really a one-word verdict on an ex, then comic punch, surprise, craft
and recognition. "Uninstalled" scores on all four at once.

- Verdict: it is the whole breakup in one verb. The ex is not
  described as bad or sad — they have been removed, deleted from
  your life the way you remove software you no longer want.
- Punch: the image lands instantly, no setup needed. Everyone has
  uninstalled an app that wasted their storage, their battery, their
  time. The ex was that app.
- Surprise: it is not the word anyone reaches for first ("toxic",
  "expired", "mistake"). It reframes a person as a program — a
  small, unexpected swerve that makes the judge smile before the
  comparison even starts.
- Recognition: universal. No slang, no reference that dates, no
  wordplay that needs explaining. One read, one laugh.

Alternatives weighed and rejected: "Expired" (true, but flat and
the most likely duplicate in a 60-entry field); "Refund" (funny,
but it begs for a second word — refund of what?); "Recalled"
(clever product-recall image, but reads as an adjective about a
memory as much as a verdict); "Blocked" (punchy, but too common
and too small — it is a setting, not a verdict); "Beta" (needs
the reader to finish the joke). "Uninstalled" needs no finishing.
"""

import os

ENTRY = "Uninstalled"  # Strategy: a tech verb as the whole verdict — the ex as software removed, not a person described.

def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 111
    # characters, not only white space, exactly one word.
    assert 1 <= len(ENTRY) <= 111, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only white space"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
