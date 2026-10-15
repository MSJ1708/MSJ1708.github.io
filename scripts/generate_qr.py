#!/usr/bin/env python3
"""Generate a QR PNG and printable portfolio card after the website is live."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

try:
    import qrcode
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Install dependencies with: python -m pip install -r requirements-dev.txt", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_URL = "https://msj1708.github.io/"
OUTPUT_DIR = ROOT / "artifacts"


def normalize_site_url(raw: str) -> str:
    parts = urlsplit(raw.strip())
    if parts.scheme != "https" or not parts.netloc:
        raise argparse.ArgumentTypeError("--site-url must be a published https:// URL")
    if parts.username or parts.password or parts.query or parts.fragment:
        raise argparse.ArgumentTypeError("--site-url must not include credentials, a query, or a fragment")
    path = parts.path.rstrip("/")
    return urlunsplit((parts.scheme, parts.netloc, path + "/", "", ""))


def load_font(size: int, bold: bool = False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"),
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(str(candidate), size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-url", default=DEFAULT_URL, help=f"Published site URL (default: {DEFAULT_URL})")
    args = parser.parse_args()
    try:
        site_url = normalize_site_url(args.site_url)
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=14, border=4)
    qr.add_data(site_url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="#192d3d", back_color="#ffffff").convert("RGB")
    qr_path = OUTPUT_DIR / "portfolio-qr.png"
    qr_image.save(qr_path)

    width, height = 1050, 600  # 3.5 x 2 inches at 300 dpi
    paper, ink, muted, accent, white = (247, 248, 246), (25, 45, 61), (95, 112, 122), (176, 88, 61), (255, 255, 255)
    canvas = Image.new("RGB", (width, height), paper)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((18, 18, width - 18, height - 18), radius=34, fill=white, outline=(220, 226, 224), width=3)
    draw.rounded_rectangle((18, 18, 36, height - 18), radius=8, fill=accent)
    draw.text((72, 78), "ENGINEERING PORTFOLIO", font=load_font(24, True), fill=accent)
    draw.text((72, 139), "Scan to explore", font=load_font(52, True), fill=ink)
    draw.text((74, 218), "Projects · Skills · Certifications", font=load_font(23), fill=muted)
    draw.line((74, 278, 475, 278), fill=(220, 226, 224), width=2)
    draw.text((74, 308), "Abdullah Khan Abdul", font=load_font(29, True), fill=ink)
    draw.text((74, 355), "Engineering · Analytics · Product", font=load_font(19), fill=muted)
    draw.text((74, 438), site_url.replace("https://", ""), font=load_font(21, True), fill=ink)
    draw.text((74, 490), "Open your phone camera and scan the code.", font=load_font(15), fill=muted)
    qr_resized = qr_image.resize((370, 370), Image.Resampling.NEAREST)
    draw.rounded_rectangle((585, 77, 1000, 492), radius=18, fill=white, outline=(232, 236, 234), width=2)
    canvas.paste(qr_resized, (600, 92))
    card_path = OUTPUT_DIR / "portfolio-qr-card.png"
    canvas.save(card_path, dpi=(300, 300))

    print(f"QR image: {qr_path}")
    print(f"Printable card: {card_path}")
    print(f"Encoded destination: {site_url}")
    print("Test the live website on a phone before printing or sharing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
