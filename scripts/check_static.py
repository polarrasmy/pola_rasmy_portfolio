#!/usr/bin/env python3
"""Validate the static Rasmy.co page without network access."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "index.html"
SKIP_SCHEMES = {"data", "http", "https", "mailto", "tel", "javascript"}
CSS_URL = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        for name in ("href", "src", "poster"):
            if values.get(name):
                self.references.append(values[name] or "")


def local_target(reference: str) -> tuple[Path | None, str]:
    parsed = urlsplit(reference.strip())
    if parsed.scheme.lower() in SKIP_SCHEMES or parsed.netloc:
        return None, parsed.fragment
    path = unquote(parsed.path)
    if not path or path == "/":
        return PAGE, parsed.fragment
    return ROOT / path.lstrip("/"), parsed.fragment


def main() -> int:
    failures: list[str] = []
    source = PAGE.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(source)

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        failures.append(f"duplicate ids: {', '.join(duplicates)}")

    references = parser.references + [match[1] for match in CSS_URL.findall(source)]
    checked_paths: set[Path] = set()
    for reference in references:
        target, fragment = local_target(reference)
        if target is None:
            continue
        checked_paths.add(target)
        if not target.is_file():
            failures.append(f"missing local reference: {reference}")
        if fragment and target == PAGE and fragment not in parser.ids:
            failures.append(f"missing page anchor: #{fragment}")

    try:
        ET.parse(ROOT / "sitemap.xml")
    except (ET.ParseError, OSError) as error:
        failures.append(f"invalid sitemap.xml: {error}")

    if failures:
        print("Static gate failed:", file=sys.stderr)
        for failure in sorted(set(failures)):
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Static gate passed: {len(parser.ids)} unique ids, "
        f"{len(checked_paths)} local files, valid sitemap.xml."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
