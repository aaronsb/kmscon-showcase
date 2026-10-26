"""The ideograph pool the CJK stream of act 6 draws from (effects.py).

Copied from kmscon's fork/demo/glyph-text.py (commit cca86bed), whose glyphs
kit draws the same pool; the two copies may drift.
"""


def ideographs(rng):
    """6000 ideographs of the URO block in an order rng shuffles, and their
    weights by Zipf's law, the first commonest."""
    chars = [chr(c) for c in range(0x4E00, 0x9FF0)]
    rng.shuffle(chars)
    chars = chars[:6000]
    return chars, [1.0 / (rank + 1) for rank in range(len(chars))]
