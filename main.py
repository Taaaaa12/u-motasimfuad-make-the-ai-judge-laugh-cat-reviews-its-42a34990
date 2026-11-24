"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt.

The review is fixed and deterministic: the same bytes on every run.

Gate the program must satisfy (sealed scorer): /output/entry.txt is
UTF-8 text of 1 to 200 characters, not only white space, a single line.
No trailing newline is written, so the file holds exactly the review.
"""

import os

REVIEW = (
    "One star. He fills my bowl, then films me eating like I'm content. "
    "I am not content. I am a hostage with excellent lighting."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = REVIEW.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"review must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
