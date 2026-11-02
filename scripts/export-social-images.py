"""Export ProdAssist landing assets to common social sizes."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
OUT = ROOT / "social-export"


BG = (15, 20, 25)  # docs/index.html --bg #0f1419


def cover_crop(im: Image.Image, tw: int, th: int) -> Image.Image:
    w, h = im.size
    scale = max(tw / w, th / h)
    nw, nh = int(w * scale), int(h * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    return im.crop((left, top, left + tw, top + th))


def fit_pad(im: Image.Image, tw: int, th: int, bg: tuple[int, int, int] = BG) -> Image.Image:
    """Scale to fit inside tw×th; pad so nothing is cropped (Instagram-safe)."""
    w, h = im.size
    scale = min(tw / w, th / h)
    nw, nh = int(w * scale), int(h * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (tw, th), bg)
    canvas.paste(im, ((tw - nw) // 2, (th - nh) // 2))
    return canvas


def main() -> None:
    OUT.mkdir(exist_ok=True)
    sources = {
        "launch-viewfinder": ASSETS / "phone-02-viewfinder.png",
        "companion": ASSETS / "phone-07-companion.png",
    }
    exports = [
        ("launch-viewfinder", 1200, 675, "x-facebook-launch-1200x675.png", "cover"),
        ("launch-viewfinder", 1080, 1350, "instagram-launch-1080x1350.png", "fit"),
        ("launch-viewfinder", 1080, 1080, "instagram-launch-1080x1080.png", "fit"),
        ("launch-viewfinder", 1080, 1920, "instagram-story-launch-1080x1920.png", "cover"),
        ("companion", 1200, 675, "x-facebook-companion-1200x675.png", "cover"),
    ]
    icon = Image.open(ASSETS / "icon-512.png").convert("RGB")
    icon.save(OUT / "profile-icon-512.png", optimize=True)

    for key, tw, th, name, mode in exports:
        im = Image.open(sources[key]).convert("RGB")
        out = fit_pad(im, tw, th) if mode == "fit" else cover_crop(im, tw, th)
        out.save(OUT / name, optimize=True, quality=90)
        print(f"wrote {name} ({mode})")


if __name__ == "__main__":
    main()
