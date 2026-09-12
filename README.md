# Expense Lens hero samples

Four hero variants for expense-lens.com that add a link to the iOS app on the App Store plus a QR code. Each variant sits on a copy of the landing page structure (floating header, hero, scroll-reveal band, extraction protocol, features, pricing, founder, FAQ, CTA, footer) so it can be judged in context.

Built in the site's own idiom: Tailwind utility classes, the site's inline style block (`css/site.css`), Space Grotesk and Geist, `iconify-icon` with lucide icons. Tailwind loads from the Play CDN here so there is no build step. The production site compiles Tailwind, so any class that is new to the site needs a CSS rebuild there.

Left out on purpose: GTM and analytics, the cookie banner, the geo pricing script, JSON-LD, the contact section, and the scroll-driven workflow animation. Page links in the header and footer are placeholders.

## Variants

- **A** `a.html` Keep the hero, add the install row. Badge and a small QR next to the existing CTA.
- **B** `b.html` Split hero with the phone. Left-aligned copy, phone screenshot, install strip with QR under the buttons.
- **C** `c.html` QR code in the lens. The lens rings become a viewfinder around the QR code.
- **D** `d.html` A on phones, B on desktop. Centered stack with the lens rings under `lg`, split layout with a larger cropped phone screenshot from `lg` up. One web CTA and one App Store badge, no pill, no install strip, no QR. New headline: "AI Receipt Scanning That Gives You Time Back."

## Behaviour

- The badge and the QR code open the App Store listing: https://apps.apple.com/us/app/expense-lens-scan-track/id6789503509
- Under 640px the QR code hides. A visitor already on a phone taps the badge. D drops the QR code everywhere.
- Scroll reveal runs at 0.35s with a near-zero intersection threshold on desktop and is off under 768px.
- The large CTA at the bottom also carries the badge.

## Editing

The pages are generated from partials:

```
src/head.html        document head, Tailwind config, grid overlay, sample switcher
src/nav.html         the floating header
src/hero-{a,b,c,d}.html
src/_lens.html       lens ring animation
src/_stats.html      stats grid
src/_h1.html         headline
src/sections.html    everything below the hero, plus the trimmed page script
build.py             assembles a.html .. d.html
```

Edit a partial, then run `python3 build.py` and commit the generated pages.

## Assets

- `assets/app-store-qr.svg` QR code for the listing URL, generated with the `qrcode` npm package, error correction M
- `assets/app-store-badge.svg` App Store badge drawn as SVG
- `assets/lens-phone.webp`, `upload-progress-phone-v2.webp`, `mileage-tracker-phone-v2.webp`, `report-*.jpg` public screenshots from the live site

## Run locally

```
python3 -m http.server 8777
```

Then open http://localhost:8777/. The site is published from the root of `main` on GitHub Pages.
