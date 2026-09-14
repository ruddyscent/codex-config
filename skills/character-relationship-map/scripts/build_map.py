#!/usr/bin/env python3
"""Starter renderer for character-relationship-map.

This intentionally keeps semantic rendering deterministic. Extend the layout
logic for the specific work rather than asking an image model to draw labels
or relationship arrows.
"""

from pathlib import Path
import argparse
import html
import yaml


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def render_svg(characters, relationships, output: Path):
    width, height = 1400, 900
    chars = characters.get("characters", [])
    rels = relationships.get("relationships", [])

    # Simple deterministic grid starter. Replace with a work-specific layout
    # once the semantic graph is verified.
    positions = {}
    cols = 4
    box_w, box_h = 280, 100
    gap_x, gap_y = 45, 70
    x0, y0 = 55, 100

    for i, char in enumerate(chars):
        col, row = i % cols, i // cols
        positions[char["id"]] = (
            x0 + col * (box_w + gap_x),
            y0 + row * (box_h + gap_y),
        )

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#faf8f3"/>',
        '<text x="50" y="55" font-family="sans-serif" font-size="30" font-weight="700">Character Relationship Map</text>',
        '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#888"/></marker></defs>',
    ]

    # Edges first so nodes cover line endpoints.
    by_id = {c["id"]: c for c in chars}
    for rel in rels:
        a, b = rel["from"], rel["to"]
        if a not in positions or b not in positions:
            continue
        ax, ay = positions[a]
        bx, by = positions[b]
        x1, y1 = ax + box_w / 2, ay + box_h / 2
        x2, y2 = bx + box_w / 2, by + box_h / 2
        label = html.escape(str(rel.get("label", rel.get("type", ""))))
        dash = ' stroke-dasharray="6 5"' if rel.get("confidence") == "TENTATIVE" else ""
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#888" stroke-width="1.5" marker-end="url(#arrow)"{dash}/>')
        svg.append(f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2-5}" text-anchor="middle" font-family="sans-serif" font-size="11" paint-order="stroke" stroke="#faf8f3" stroke-width="4">{label}</text>')

    for char in chars:
        x, y = positions[char["id"]]
        name = html.escape(str(char["name"]))
        desc = html.escape(str(char.get("description", "")))
        tentative = char.get("confidence") == "TENTATIVE"
        dash = ' stroke-dasharray="6 5"' if tentative else ""
        svg.append(f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="10" fill="#fff" stroke="#777"{dash}/>')
        svg.append(f'<text x="{x+14}" y="{y+30}" font-family="sans-serif" font-size="18" font-weight="700">{name}</text>')
        svg.append(f'<text x="{x+14}" y="{y+58}" font-family="sans-serif" font-size="12">{desc}</text>')

    svg.append('</svg>')
    output.write_text("\n".join(svg), encoding="utf-8")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--characters", type=Path, required=True)
    p.add_argument("--relationships", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    render_svg(load_yaml(args.characters), load_yaml(args.relationships), args.output)


if __name__ == "__main__":
    main()
