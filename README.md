# Engineering Portfolio

A responsive, single-page portfolio for Abdullah Khan Abdul. The complete website is in `index.html`, with built-in styling and JavaScript. It needs no build process, database, visitor account, or paid hosting.

## Publish free with GitHub Pages

The planned public address is **https://msj1708.github.io/**.

1. Open this repository's **Settings → Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Choose branch **main** and folder **/(root)**, then press **Save**.
4. Wait for GitHub Pages to publish the site, then open https://msj1708.github.io/ on your phone and test the navigation and project filters.

GitHub Pages is available for public repositories on GitHub Free. Initial publication can take a few minutes. Until you enable Pages and verify the site opens, the address should be treated as planned, not confirmed live. Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## QR code and card

The repository includes a generator at `scripts/generate_qr.py`. After the site is published, run these commands in a terminal from the repository folder:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_qr.py --site-url https://msj1708.github.io/
```

It creates a standalone QR and a print-ready business card under `artifacts/`. Test the published site from a phone before printing or handing out cards. A QR code opens the website directly; it does not publish the site.

## Portfolio sections

- **Projects:** SIE (short name only), Project AEGIS, manufacturing simulation, inventory optimization, production-line optimization, transportation optimization, SHO Live Translation, and private R&D.
- **Certifications:** Project Management, Lean Six Sigma White Belt, and Lean Manufacturing (Alison), based on information supplied by the owner.
- **Skills, About, and Contact:** skill groups, professional introduction, and public GitHub links.

## Editing

Edit `index.html` to change the content, styling, project filters, or navigation.

## Privacy

This is a public portfolio, not a password-protected site. Anyone with its URL or QR can view it. The SIE card is kept high-level and has no source-code link; its independent GitHub repository visibility must be managed separately.
