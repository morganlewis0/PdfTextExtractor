import argparse
from pathlib import Path

from .core import extract_text


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Extract text from a PDF to stdout or file")
    p.add_argument("pdf", type=Path, help="Input PDF path")
    p.add_argument("-o", "--out", type=Path, help="Output .txt path (defaults to stdout)")
    p.add_argument("--pages", type=str, help="Page ranges like 1,3-5 (1-indexed)")
    return p


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    pages = None
    if args.pages:
        pages = []
        for part in args.pages.split(","):
            if "-" in part:
                a, b = part.split("-", 1)
                pages.extend(range(int(a), int(b) + 1))
            else:
                pages.append(int(part))

    text = extract_text(args.pdf, pages=pages)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
