from pathlib import Path
from src.pdf_text_extractor.core import extract_text


def test_missing_file_returns_empty(tmp_path: Path):
    fake = tmp_path / "missing.pdf"
    assert extract_text(fake) == ""

def test_existing_file_without_pdfminer_returns_placeholder(tmp_path: Path):
    f = tmp_path / "dummy.pdf"
    f.write_bytes(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    out = extract_text(f, pages=[1, 2])
    assert isinstance(out, str)
