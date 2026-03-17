# ActuallyRandomBibleQuotes — PWA

A minimal Progressive Web App that displays a random verse from the American Standard Version of the Bible. Works on Android and iPhone — installable to the home screen like a native app.

## Files

| File            | Purpose                                    |
|-----------------|-------------------------------------------|
| `index.html`    | The entire app (HTML + CSS + JS)          |
| `asv.txt`       | ASV Bible text — one verse per line       |
| `manifest.json` | PWA manifest (name, icons, theme)         |
| `sw.js`         | Service worker (offline caching)          |
| `icon-192.png`  | Home screen icon (192×192)                |
| `icon-512.png`  | Splash screen icon (512×512)              |

## Setup

1. **Get asv.txt**: Place your ASV Bible text file (one verse per line) in the same folder as `index.html`. Name it `asv.txt`.

2. **Deploy** to any free static host:
   - **Netlify**: Drag & drop the folder at netlify.com
   - **GitHub Pages**: Push to a repo, enable Pages in Settings
   - **Cloudflare Pages**: Connect your repo at pages.cloudflare.com

3. **Install on your phone**:
   - **Android**: Open the URL in Chrome, tap the menu, then "Install app"
   - **iPhone**: Open in Safari, tap Share, then "Add to Home Screen"

The app works offline once installed — the entire Bible text is cached by the service worker.
