"""One-line roast for make.fun: the laptop charger that only works at a magic angle.

Roasts a gadget used every day (the laptop charger) with one specific,
concrete detail — the cable has to be bent at exactly 37 degrees — and a
punchline at the end. Writes the single line to /output/entry.txt.
"""
import os

LINE = "My laptop charger only works if I bend the cable at exactly 37 degrees — I've been holding a yoga pose for my own hardware since 2023."

def main():
    # Gate self-check: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
