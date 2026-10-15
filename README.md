# Engineering Portfolio

A lightweight, responsive single-page portfolio for Abdullah Khan Abdul. It uses static HTML, CSS and JavaScript; there is no build step, server, database, or visitor sign-in.

## Publish free with GitHub Pages

This repository is intended to publish at **https://msj1708.github.io/**.

1. Open **Settings → Pages** in this repository.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch **main** and folder **/(root)**, then save.
4. Wait for GitHub Pages to finish deploying, then test https://msj1708.github.io/ on your phone.

The QR card in this repository encodes that URL. Test the live site before printing the card.

## Portfolio contents

The portfolio showcases selected engineering simulation, optimization and product projects, skills, the three certifications provided by the owner, an About section, and public GitHub contact links. The industrial platform that the owner wishes to keep discreet is labelled only **SIE** and is not linked to its source repository.

## QR card

The PNG files `Portfolio-QR.png` and `Portfolio-QR-Card.png` contain the QR code and printable landscape card. To regenerate after changing the final URL:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_qr.py --site-url https://your-live-site.example/
```

## Privacy

This is a public portfolio, not a password-protected website. Anyone who has the URL or scans the QR can see it. Hiding a repository link here does not change that repository's separate GitHub visibility.
