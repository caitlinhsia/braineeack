"""Wrap src/game.html (page body, as published to the claude.ai artifact) into a standalone index.html for static hosting."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / "src" / "game.html").read_text()
split = src.index('<div class="wrap">')
head, body = src[:split].strip(), src[split:].strip()
fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
       "%3Crect width='32' height='32' rx='7' fill='%23121628'/%3E"
       "%3Crect x='5' y='5' width='10' height='10' rx='3' fill='%23ff6b5e'/%3E"
       "%3Crect x='17' y='5' width='10' height='10' rx='3' fill='%23ffd24f'/%3E"
       "%3Crect x='5' y='17' width='10' height='10' rx='3' fill='%2347d4b5'/%3E"
       "%3Crect x='17' y='17' width='10' height='10' rx='3' fill='%23b08eff'/%3E%3C/svg%3E")
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="An adaptive brain-training game: a daily World Tour, food and fashion map guessers, dress design, sewing, floorplans, mediation dramas, and memory, math, word and logic games.">
<meta name="theme-color" content="#121628">
<link rel="icon" href="{fav}">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}img{{max-width:100%}}</style>
{head}
</head>
<body>
{body}
</body>
</html>
"""
(root / "index.html").write_text(page)
print(f"index.html written ({len(page):,} bytes)")
