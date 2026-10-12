# VacantSpace Frontend

Beginner-friendly multi-page student lounge website using HTML, CSS, and PyScript only.

## Pages and files
- `index.html` — Home page and large photo hero
- `spaces.html` — Chill Zone and separate Quiet Study Room
- `pricing.html` — Sample rates and PyScript price estimator
- `about.html` — Business concept
- `css/style.css` — Shared design and responsive layout
- `pyscript/main.py` — Python event handlers for the estimator

## Run in VS Code
1. Extract/open this folder in VS Code.
2. Install/use the Live Server extension, then open `index.html` with Live Server.
3. Use the navigation to open the other pages.
4. Open Pricing and test Calculate price and Reset.

Internet access is needed for PyScript, Google Fonts, and the sample photos because these load from external URLs.

## Easy updates
- Change the hourly rates in `pyscript/main.py` inside `RATES`.
- Update the visible sample rates in `pricing.html` so they match.
- Change photo URLs in each HTML page.
- Edit colors, spacing, fonts, and responsive rules in `css/style.css`.

## Note
Frontend prototype only. It does not store data, reserve seats, or accept payments. Prices are placeholders, not final business recommendations.
