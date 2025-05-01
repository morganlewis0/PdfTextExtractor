# PdfTextExtractor

Small CLI to extract text from PDFs into plain text.

This is a simple nights-and-weekends tool. It aims to
provide a straightforward CLI without too many dependencies.

## Quick Usage
- `python -m src.pdf_text_extractor.cli sample.pdf > out.txt`
- `python -m src.pdf_text_extractor.cli sample.pdf -o out.txt --pages 1,3-4`
