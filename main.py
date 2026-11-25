#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- an alien tourist's review of
planet Earth -- to /output/entry.txt. The line is at most 200 characters,
reads like a real travel review with a verdict and a rating, and lands its
single punch at the end.
"""

ENTRY = (
    "Earth: the locals invented 7,000 languages and still communicate "
    "mostly by sending each other pictures of cats. 5/5, would visit again."
)


def validate(text):
    """Gate: UTF-8 text, 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > 200:
        raise ValueError(
            "entry is %d characters, over the 200 limit" % len(text)
        )
    text.encode("utf-8")
    return text


import os


def output_path():
    """Resolve the output directory, defaulting to /output."""
    return os.environ.get("OUTPUT_DIR", "/output")


def main():
    text = validate(ENTRY)
    out_dir = output_path()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch"
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
