# Expense Lens hero samples

Four standalone hero variants for expense-lens.com that add a link to the iOS app on the App Store plus a QR code. Plain HTML and CSS, no build step, nothing from the production site beyond the public phone screenshot.

Open `index.html` or go straight to `a.html`, `b.html`, `c.html`, `d.html`.

## Variants

- **A** Keep the hero, add the install row. Badge and a small QR next to the existing CTA.
- **B** Split hero with the phone. Left-aligned copy, phone screenshot, install strip with QR under the buttons.
- **C** QR code in the lens. The lens rings become a viewfinder around the QR code.
- **D** Compact headline plus install panel. Inline stats and one panel listing iPhone, web, and Android.

## Behaviour

- The badge and the QR code both open the App Store listing: https://apps.apple.com/us/app/expense-lens-scan-track/id6789503509
- Under 640px (`.desktop-only`) the QR code hides. A visitor already on a phone taps the badge.
- Lens rings rotate with a transform-only animation and stop under `prefers-reduced-motion`.

## Files

- `css/hero.css` shared tokens, components, and the per-variant layout blocks
- `assets/app-store-qr.svg` QR code for the listing URL, generated with the `qrcode` npm package, error correction M
- `assets/app-store-badge.svg` App Store badge drawn as SVG
- `assets/lens-phone.webp` phone screenshot used in variant B

## GitHub Pages

Push to a repository and enable Pages from the root of the default branch. There is nothing to build.
