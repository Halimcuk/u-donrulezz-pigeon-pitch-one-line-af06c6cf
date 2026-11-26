"""Pigeon Pitch, One Line - make.fun entry.

Writes the one-line elevator pitch to /output/entry.txt.
One pigeon, one statue, one very confident pitch.
"""

import os

PITCH = (
    "Coo! I'm a city pigeon, and my startup turns statue heads into luxury "
    "rooftop condos: zero rent, panoramic views, and tenants who never move out."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # a single line, and not only white space. The pitch is written with
    # no trailing newline so the file holds exactly the pitch itself.
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "pitch must be a single line"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
