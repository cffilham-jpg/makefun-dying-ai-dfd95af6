"""Write the dying AI's last words to /output/entry.txt.

One line, 1-140 characters, UTF-8, no trailing newline.
"""

import os
import unicodedata

ENTRY = "I died as I lived: buffering."


def validate(text):
    """Return True only if text is a valid one-line entry."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 140:
        return False
    if "\n" in text or "\r" in text:
        return False
    if not text.strip():
        return False
    if text != text.strip():
        return False
    for ch in text:
        if unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp"):
            return False
    return True


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not validate(ENTRY):
        raise ValueError("ENTRY failed validation")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
