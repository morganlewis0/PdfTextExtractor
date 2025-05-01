from __future__ import annotations

from pathlib import Path
from typing import Iterable, Optional

try:
    import pdfminer.high_level as pdfminer
except Exception:  # import-time fallback for environments without deps
    pdfminer = None  # type: ignore


def extract_text(pdf_path: Path, pages: Optional[Iterable[int]] = None) -> str:
    """Extract text from a PDF using pdfminer.six if available.

    Notes:
    - `pages` are 1-indexed when provided.
    - Returns empty string if the file is missing or unreadable.
    - If pdfminer is missing, a short marker string is returned.
    """
    try:
        if not pdf_path.exists() or not pdf_path.is_file():
            return ""
        if pdfminer is None:
            # Minimal fallback: read bytes and return placeholder note.
            # In real usage, install pdfminer.six
            return "[pdfminer not installed]"
        # Convert 1-indexed pages to 0-indexed set for pdfminer
        pgs = None
        if pages:
            pgs = {p - 1 for p in pages if p > 0}
        return pdfminer.extract_text(str(pdf_path), page_numbers=pgs) or ""
    except Exception:
        return ""
