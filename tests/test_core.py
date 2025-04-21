from pathlib import Path
from src.pdf_text_extractor.core import extract_text


def test_missing_file_returns_empty(tmp_path: Path):
    fake = tmp_path / "missing.pdf"
    assert extract_text(fake) == ""
